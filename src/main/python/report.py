from settings.default import TOKEN
from client import *
from stock import *
from financial_statement import *
from utils import *
from openpyxl import Workbook
from openpyxl.styles import PatternFill, Border, Side, Alignment, Protection, Font
from openpyxl.styles.differential import DifferentialStyle
from openpyxl.formatting.rule import Rule
from openpyxl.utils import get_column_letter
from openpyxl.utils.dataframe import dataframe_to_rows
from openpyxl.worksheet.table import Table, TableStyleInfo
from pathlib import Path
import tempfile


style = TableStyleInfo(name="TableStyleMedium9", showFirstColumn=False,
                       showLastColumn=False, showRowStripes=True, showColumnStripes=True)


class StockReport:

    def __init__(self, stock: Stock):
        self.__stock = stock
        self.__wb = Workbook()

    def __write_company_info(self):
        data = self.__stock.get_company()
        ws = self.__wb.active
        ws.title = f"{self.__stock.get_ticker()}"

        for r in dataframe_to_rows(data, index=True, header=False):
            ws.append(r)
        fit_width(ws)

    def __write_to_balance_sheet_to_excel(self):
        data = self.__stock.get_balance_sheet()
        ws = self.__wb.create_sheet("BalanceSheet")

        for r in dataframe_to_rows(data, index=True, header=True):
            ws.append(r)
        fit_width(ws)
        tab = Table(displayName="IncomeStatement", ref=f"A1:{get_column_letter(ws.max_column)}{ws.max_row}")
        tab.tableStyleInfo = style
        ws.add_table(tab)

    def __write_to_income_statement_to_excel(self):
        data = self.__stock.get_income_statement()
        ws = self.__wb.create_sheet("IncomeStatement")
        for r in dataframe_to_rows(data, index=True, header=True):
            ws.append(r)

        fit_width(ws)
        tab = Table(displayName="IncomeStatement", ref=f"A1:{get_column_letter(ws.max_column)}{ws.max_row}")
        # Add a default style with striped rows and banded columns
        tab.tableStyleInfo = style
        ws.add_table(tab)

    def generate(self, filename, directory="output"):
        self.__write_company_info()
        self.__write_to_balance_sheet_to_excel()
        self.__write_to_income_statement_to_excel()

        path = Path(f'{directory}/{filename}.xlsx')
        path.parent.mkdir(parents=True, exist_ok=True)

        self.__wb.save(path)


