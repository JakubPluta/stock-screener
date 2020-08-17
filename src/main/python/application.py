import argparse
import os
from report import StockReport
from stock import *


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--api_key",
        dest="api_key",
        type=str,
        help="finnhub api_key",
        default=os.environ.get("FH_API_KEY"),
        required=False,
    )
    parser.add_argument(
        "--ticker",
        dest="ticker",
        type=str,
        help="stock company ticker like AAPL",
        required=True,
    )
    parser.add_argument(
        "--directory",
        dest="directory",
        type=str,
        help="output dictionary",
        required=False,
        default="output",
    )
    parser.add_argument(
        "--filename",
        dest="filename",
        type=str,
        help="filename",
        required=False,
        default="FinancialReport",
    )
    args = parser.parse_args()
    stock_creator = StockCreator(args.ticker, args.api_key)
    stock = stock_creator.create_stock()
    report = StockReport(stock)
    report.generate(args.filename, args.directory)
