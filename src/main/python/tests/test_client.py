from client import FinnhubClient
from stock import StockCreator
from report import StockReport
from settings.default import TOKEN
import os


def test_report_is_generated():
    company = "FB"
    stock_creator = StockCreator(company, TOKEN)
    stock = stock_creator.create_stock()
    report = StockReport(stock)
    report.generate(filename="Financial Report")
    assert os.path.isfile(report._StockReport__output)
