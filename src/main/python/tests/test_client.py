from client import FinnhubClient
from stock import StockCreator
from settings.default import TOKEN
import pandas as pd

def test_client_should_fetch_financial_statement():
    # given
    company = 'AAPL'
    client = FinnhubClient(TOKEN)
    client.show_endpoints()
    financial_statement = client.fetch_financial_statement_as_reported(company)
    data = financial_statement.get('data')
    balance_sheet = []
    
    for record in data:
        bs = pd.DataFrame(record['report']['bs'])
        bs['year'] = record.get('year')
        bs['symbol'] = record.get('symbol')
        balance_sheet.append(bs)
    results = pd.concat(balance_sheet,ignore_index=True) [['symbol','year','label','value']]   
    results['value'] = pd.to_numeric(results['value'], errors='coerce')
    results = results.pivot_table(index='label', columns='year', values='value')
    
    assert results is not None
    assert isinstance(results,pd.DataFrame)



def test_stock_creator_should_create_stock():
    company = 'AAPL'
    
    stock_creator = StockCreator(company)
    
    assert stock_creator