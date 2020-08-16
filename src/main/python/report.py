from stock import *
from utils import *
from openpyxl import Workbook
from pathlib import Path


class StockReport:

    def __init__(self, stock: Stock):
        self.__stock = stock
        self.__wb = Workbook()
        self.__output = None

    def __write_company_info(self):
        data = self.__stock.get_company()
        ws = self.__wb.active
        ws.title = f"{self.__stock.get_ticker()[0]}"
        write_data_frame_to_rows(ws, data, False)
        format_ws_borders(ws)
        format_ws(ws)

    def __write_balance_sheet_to_excel(self):
        data = self.__stock.get_balance_sheet()
        ws = self.__wb.create_sheet("BalanceSheet")
        write_data_frame_to_rows(ws, data)
        ws.delete_rows(2, 1)
        format_ws(ws)

    def __write_income_statement_to_excel(self):
        data = self.__stock.get_income_statement()
        ws = self.__wb.create_sheet("IncomeStatement")
        write_data_frame_to_rows(ws, data)
        ws.delete_rows(2, 1)
        format_ws(ws)

    def __write_cash_flow_to_excel(self):
        data = self.__stock.get_cash_flow()
        ws = self.__wb.create_sheet("CashFlow")
        write_data_frame_to_rows(ws, data)
        ws.delete_rows(2, 1)
        format_ws(ws)

    def __write_metrics_to_excel(self):
        data = self.__stock.get_key_stats()
        ws = self.__wb.create_sheet("KeyMetrics")
        write_data_frame_to_rows(ws, data)
        ws.delete_rows(2, 1)
        format_ws(ws)

    def generate(self, filename, directory="output"):
        self.__write_company_info()
        self.__write_balance_sheet_to_excel()
        self.__write_income_statement_to_excel()
        self.__write_cash_flow_to_excel()
        self.__write_metrics_to_excel()

        path = Path(f'{directory}/{filename}.xlsx')
        path.parent.mkdir(parents=True, exist_ok=True)
        self.__output = path

        print(f"Report was generated and save {path}")
        self.__wb.save(path)


