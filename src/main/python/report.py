from settings.default import TOKEN
from client import *
from stock import *
from financial_statement import *
from utils import *


class StockReport:
    def __init__(self, stock: Stock):
        self.__stock = stock
        self.__element_name = ""
        self.__file_name = f"{self.__element_name}{self.__element_name}_stock_report.xlsx"

    def save_income_statement(self):
        self.__element_name  = "Income Statement"
        self.__stock.get_income_statement().to_excel(self.__file_name)

    def save_balance_sheet(self):
        self.__element_name = "Balance Sheet"
        self.__stock.get_balance_sheet().to_excel(self.__file_name)

    def save_cash_flow(self):
        self.__element_name = "Cash Flow"
        self.__stock.get_cash_flow().to_excel(self.__file_name)

    def save_metrics(self):
        self.__element_name = "Metrics"
        self.__stock.get_key_stats().to_excel(self.__file_name)

    def save_company_profile(self):
        self.__element_name = "Company Profile"
        self.__stock.get_key_stats().to_excel(self.__file_name)