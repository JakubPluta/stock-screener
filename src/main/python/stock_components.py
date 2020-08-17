import pandas as pd
from client import FinnhubClient


class FinancialStatement:
    financial_elements = ["bs", "ic", "cf"]

    def __init__(self, ticker, client: FinnhubClient):
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
        results = results.pivot_table(index="label", columns="year", values="value")
        results.columns = results.columns.astype(str)
        return results.reset_index()

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
        data = pd.json_normalize(self.__data).T
        return data.reset_index()

    def get_company(self):
        return self.__company


class KeyMetrics:
    def __init__(self, ticker, client: FinnhubClient):
        self.__ticker = ticker
        self.__data = client.fetch_key_metrics(self.__ticker)
        self.__key_metrics = self.__extract_key_metrics()

    def __extract_key_metrics(self):
        return (
            pd.json_normalize(self.__data.get("metric"))
            .T.reset_index()
            .rename(columns={"index": "KPI", 0: "Value"})
        )

    def get_key_metrics(self):
        return self.__key_metrics


class CompanyNews:
    def __init__(self, ticker, client: FinnhubClient):
        self.__ticker = ticker
        self.__data = client.fetch_company_news(self.__ticker)
        self.__company_news = self.__extract_company_news()

    def __extract_company_news(self):
        data = pd.json_normalize(self.__data).reset_index()[
            ["datetime", "headline", "summary"]
        ]
        data["datetime"] = pd.to_datetime(data["datetime"], unit="s")
        return data

    def get_company_news(self):
        return self.__company_news


class NewsSentiment:
    def __init__(self, ticker, client: FinnhubClient):
        self.__ticker = ticker
        self.__data = client.fetch_news_sentiments(self.__ticker)
        self.__sentiments = self.__extract_sentiments()

    def __extract_sentiments(self):
        data = pd.json_normalize(self.__data).T
        return data.reset_index()

    def get_sentiments(self):
        return self.__sentiments


class SEC:
    def __init__(self, ticker, client: FinnhubClient):
        self.__ticker = ticker
        self.__data = client.fetch_sec_fillings(self.__ticker)
        self.__sec_fillings = self.__extract_sec_fillings()

    def __extract_sec_fillings(self):
        data = pd.json_normalize(self.__data)
        return data.reset_index()

    def get_sec_fillings(self):
        return self.__sec_fillings


class Recommendations:
    def __init__(self, ticker, client: FinnhubClient):
        self.__ticker = ticker
        self.__data = client.fetch_recommendations(self.__ticker)
        self.__recommendations = self.__extract_recommendations()

    def __extract_recommendations(self):
        return pd.json_normalize(self.__data).reset_index()

    def get_recommendations(self):
        return self.__recommendations


class Quote:
    def __init__(self, ticker, client: FinnhubClient):
        self.__ticker = ticker
        self.__data = client.fetch_quote(self.__ticker)
        self.__quote = self.__extract_quote()

    def __extract_quote(self):
        data = pd.DataFrame(self.__data)
        data = data.rename(
            columns={
                "o": "Open",
                "h": "High",
                "c": "Close",
                "v": "Volume",
                "t": "Date",
                "l": "Low",
            }
        )
        data["Date"] = pd.to_datetime(data["Date"], unit="s")

        return data[["Date", "Open", "Low", "High", "Close", "Volume"]]

    def get_quote(self):
        return self.__quote
