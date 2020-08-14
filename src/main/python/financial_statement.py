import pandas as pd


class BalanceSheet:

    def __init__(self, data):
        self.__data = data
        self.balance_sheet = self.__extract_balance_sheet()

    def get_data(self):
        return self.__data

    def get_balance_sheet(self):
        return self.balance_sheet

    def __extract_balance_sheet(self):
        financial_statement = self.__data.get('data')
        balance_sheet = []
        for record in financial_statement:
            bs = pd.DataFrame(record['report']['bs'])
            bs['year'] = record.get('year')
            bs['symbol'] = record.get('symbol')
            balance_sheet.append(bs)
        results = pd.concat(balance_sheet, ignore_index=True)[['symbol', 'year', 'label', 'value']]
        results['value'] = pd.to_numeric(results['value'], errors='coerce')
        return results.pivot_table(index='label', columns='year', values='value')


