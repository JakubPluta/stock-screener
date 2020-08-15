import pandas as pd
from client import FinnhubClient


class FinancialStatement:
    financial_elements = ["bs", "ic", "cf"]

    def __init__(self, ticker, client: FinnhubClient ):
        self.__ticker = ticker
        self.__data = client.fetch_financial_statement_as_reported(self.__ticker)
        (
            self.__balance_sheet,
            self.__income_statement,
            self.__cash_flow_statement,
        ) = self.extract_elements_of_financial_statement()

    def __object_extractor(self, element: str):
        data = self.__data.get("data")
        financial_statement_element = []

        for record in data:
            statement_element = pd.DataFrame(record["report"][f"{element}"])
            statement_element["year"] = record.get("year")
            statement_element["symbol"] = record.get("symbol")
            financial_statement_element.append(statement_element)

        results = pd.concat(financial_statement_element, ignore_index=True)[
            ["symbol", "year", "label", "value"]
        ]
        results["value"] = pd.to_numeric(results["value"], errors="coerce")
        return results.pivot_table(index="label", columns="year", values="value")

    def extract_elements_of_financial_statement(self):
        financial_statement = []
        for ele in self.financial_elements:
            financial_statement.append(self.__object_extractor(ele))
        return financial_statement

    def get_balance_sheet(self):
        return self.__balance_sheet

    def get_income_statement(self):
        return self.__income_statement

    def get_cash_flow(self):
        return self.__cash_flow_statement


class CompanyProfile:
    def __init__(self, ticker, client: FinnhubClient):
        self.__ticker = ticker
        self.__data = client.fetch_company(self.__ticker)
        self.__company = self.__extract_company()

    def __extract_company(self):
        return pd.json_normalize(self.__data).T

    def get_company(self):
        return self.__company
