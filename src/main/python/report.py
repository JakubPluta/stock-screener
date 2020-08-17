from stock import *
from utils import *
from openpyxl import Workbook
from pathlib import Path


class StockReport:
    def __init__(self, stock: Stock):
        self.__stock = stock
        self.__wb = Workbook()
        self.__output = None

    def __create_first_page(self):
        #TODO add a first page
        pass

    def __delete_first_empty_page(self):
        try:
            del self.__wb['Sheet']
        except ValueError:
            print("Sheet not found")

    def __write_elements_into_excel(self):
        for key, data in self.__stock.get_all_elements_of_stock().items():
            ws = self.__wb.create_sheet(str(key))
            write_data_frame_to_rows(ws, data)
            format_ws(ws)

    def generate(self, filename, directory="output"):
        self.__write_elements_into_excel()
        self.__delete_first_empty_page()
        path = Path(f"{directory}/{filename}.xlsx")
        path.parent.mkdir(parents=True, exist_ok=True)
        self.__output = path

        print(f"Report was generated and save {path}")
        self.__wb.save(path)
