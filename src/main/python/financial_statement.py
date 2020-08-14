import pandas as pd


class FinancialStatement:
    financial_elements = ["bs", "ic", "cf"]

    def __init__(self, data):
        self.__data = data
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


class BalanceSheet:
    def __init__(self, data):
        self.__data = data
        self.balance_sheet = self.__extract_balance_sheet()

    def get_data(self):
        return self.__data

    def get_balance_sheet(self):
        return self.balance_sheet

    def __extract_balance_sheet(self):
        financial_statement = self.__data.get("data")
        balance_sheet = []
        for record in financial_statement:
            bs = pd.DataFrame(record["report"]["bs"])
            bs["year"] = record.get("year")
            bs["symbol"] = record.get("symbol")
            balance_sheet.append(bs)
        results = pd.concat(balance_sheet, ignore_index=True)[
            ["symbol", "year", "label", "value"]
        ]
        results["value"] = pd.to_numeric(results["value"], errors="coerce")
        return results.pivot_table(index="label", columns="year", values="value")
