from client import FinnhubClient
from settings.default import TOKEN
from stock_components import *


class StockCreator:
    def __init__(self, ticker, api_key):
        self.ticker = ticker
        self.__client = FinnhubClient(api_key)
        self.__financial_statement = FinancialStatement(self.ticker, self.__client)
        self.__metrics = KeyMetrics(self.ticker, self.__client)
        self.__company = CompanyProfile(self.ticker, self.__client)
        self.__quote = Quote(self.ticker, self.__client)
        self.__company_news = CompanyNews(self.ticker, self.__client)
        self.__recommendations = Recommendations(self.ticker, self.__client)
        self.__sec_fillings = SEC(self.ticker, self.__client)
        self.__stock: Stock

    def create_stock(self):
        ticker = (self.ticker,)
        company = self.__company.get_company()
        balance_sheet = self.__financial_statement.get_balance_sheet()
        income_statement = self.__financial_statement.get_income_statement()
        cash_flow = self.__financial_statement.get_cash_flow()
        stats = self.__metrics.get_key_metrics()
        recommendations = self.__recommendations.get_recommendations()
        quote = self.__quote.get_quote()
        company_news = self.__company_news.get_company_news()
        sec_fillings = self.__sec_fillings.get_sec_fillings()

        return Stock(
            ticker,
            company,
            balance_sheet,
            income_statement,
            cash_flow,
            stats,
            recommendations,
            quote,
            company_news,
            sec_fillings,
        )


class Stock:
    def __init__(
        self,
        ticker,
        company,
        balance_sheet,
        income_statement,
        cash_flow,
        stats,
        recommendations,
        quote,
        company_news,
        sec_fillings,
    ):
        self.__ticker: str = ticker
        self.__company: pd.DataFrame = company
        self.__balance_sheet: pd.DataFrame = balance_sheet
        self.__income_statement: pd.DataFrame = income_statement
        self.__cash_flow: pd.DataFrame = cash_flow
        self.__stats: pd.DataFrame = stats
        self.__company_news = company_news
        self.__recommendations = recommendations
        self.__quote = quote
        self.__sec_fillings = sec_fillings
        self.__elements = {}
        self.__create_dict_of_all_elements()

    def __str__(self):
        return f"Data found for {self.__ticker[0]}"

    def __create_dict_of_all_elements(self):
        self.__elements["Company"] = self.__company
        self.__elements["BalanceSheet"] = self.__balance_sheet
        self.__elements["IncomeStatement"] = self.__income_statement
        self.__elements["CashFlow"] = self.__cash_flow
        self.__elements["Stats"] = self.__stats
        self.__elements["CompanyNews"] = self.__company_news
        self.__elements["Recommendations"] = self.__recommendations
        self.__elements["Quote"] = self.__quote
        self.__elements["SecFillings"] = self.__sec_fillings

    def get_all_elements_of_stock(self):
        return self.__elements

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

    def get_recommendations(self):
        return self.__recommendations

    def get_quote(self):
        return self.__quote

    def get_company_news(self):
        return self.__company_news

    def get_sec_fillings(self):
        return self.__sec_fillings
