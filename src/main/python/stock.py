from client import FinnhubClient
from settings.default import TOKEN
from financial_statement import *


class StockCreator:
    def __init__(self, ticker):
        self.ticker = ticker
        self.__client = FinnhubClient(TOKEN)
        self.__financial_statement = FinancialStatement(self.ticker, self.__client)
        self.__metrics = KeyMetrics(self.ticker, self.__client)
        self.__company = CompanyProfile(self.ticker, self.__client)
        self.__stock: Stock

    def create_stock(self):
        ticker = self.ticker,
        company = self.__company.get_company()
        balance_sheet = self.__financial_statement.get_balance_sheet()
        income_statement = self.__financial_statement.get_income_statement()
        cash_flow = self.__financial_statement.get_cash_flow()
        stats = self.__metrics.get_key_metrics()

        return Stock(ticker, company, balance_sheet, income_statement, cash_flow, stats)


class Stock:
    def __init__(
        self, ticker, company, balance_sheet, income_statement, cash_flow, stats
    ):
        self.__ticker: str = ticker
        self.__company: pd.DataFrame = company
        self.__balance_sheet: pd.DataFrame = balance_sheet
        self.__income_statement: pd.DataFrame = income_statement
        self.__cash_flow: pd.DataFrame = cash_flow
        self.__stats: pd.DataFrame = stats

    def __str__(self):
        return f"Data found for {self.__ticker}"

    def __verify_stocks(self):
        pass

    def get_ticker(self):
        return self.__ticker

    def set_ticker(self, ticker):
        self.__ticker = ticker

    def get_company(self):
        return self.__company

    def set_company(self, company):
        self.__company = company

    def get_balance_sheet(self):
        return self.__balance_sheet

    def set_balance_sheet(self, balance_sheet):
        self.__balance_sheet = balance_sheet

    def get_income_statement(self):
        return self.__income_statement

    def set_income_statement(self, income_statement):
        self.__income_statement = income_statement

    def get_cash_flow(self):
        return self.__cash_flow

    def set_cash_flow(self, cash_flow):
        self.__cash_flow = cash_flow

    def get_key_stats(self):
        return self.__stats

    def set_key_stats(self, stats):
        self.__stats = stats
