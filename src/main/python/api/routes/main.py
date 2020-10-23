import pandas as pd
from api import db
from flask import render_template, url_for, flash, redirect, request, Blueprint, send_from_directory, send_file
from api.models import Symbol
from api.forms import SymbolForm

from client import FinnhubClient
from stock import StockCreator
from report import StockReport
from settings.default import TOKEN
import os


main = Blueprint('main', __name__)


@main.route('/')
def home():
    return render_template('home.html')

@main.route('/success')
def success():
    return render_template('success.html')


@main.route('/report', methods=['GET','POST'])
def report():
    form = SymbolForm()
    if form.validate_on_submit():
        company = form.data.get('symbol')
        if bool(Symbol.query.filter_by(ticker=company).first()):
            try:
                stock_creator = StockCreator(company, TOKEN)
                stock = stock_creator.create_stock()
                report = StockReport(stock)
                report.generate(filename="Financial Report")
                path = os.path.join(report._StockReport__output)
                return send_file(path, as_attachment=True)
            except:
                flash('Provided company doesnt exists')
                redirect(url_for('main.report'))
        else:
            flash('Provided company doesnt exists')
            redirect(url_for('main.report'))
    return render_template('report.html', form=form)



@main.route('/about')
def about():
    return render_template('about.html')


@main.route('/symbols')
def symbols():
    symbols = Symbol.query.all()
    return render_template('tickers.html', symbols=symbols)



# Debug
@main.route('/debug_stock_exchanges')
def get_stock_exchanges():
    df = pd.read_csv(r'C:\Repository\priv\stock-screener\src\main\python\symbols\all_symbols.csv')
    df = df[['code','name']]
    return df


@main.route('/debug_all_symbols')
def get_all_symbols():
    df_nasdaq = pd.read_csv(r'C:\Repository\priv\stock-screener\src\main\python\symbols\nasdaq_stocks.csv'
                            , usecols=['Symbol','Name'])
    df_nyse = pd.read_csv(r'C:\Repository\priv\stock-screener\src\main\python\symbols\nyse_stocks.csv'
                          , usecols=['Symbol','Name'])
    
    df = pd.concat([df_nasdaq, df_nyse],ignore_index=True)
    df = df.drop_duplicates(subset=['Symbol','Name'])
    df[['Symbol', 'Name']].sort_values(by='Symbol', ascending=True)
    df = df.reset_index(drop=False)
    return df[['Symbol', 'Name']]


@main.route('/debug_add_to_db')
def add_symbols():
    stocks = get_all_symbols()
    for index, stock in stocks.iterrows():
        symbol = Symbol(ticker=stock.get('Symbol'),name=stock.get('Name'))
        db.session.add(symbol)
    db.session.commit()
    return 'Db added'


