# Stock Screener Reports

Simple application that generates Excel reports with some stock company data


### Prerequisites

```
visit https://finnhub.io/ and get your API key
```

### Installing


```
git clone https://github.com/JakubPluta/stock-screener.git
pip install -r requirements
```

## Running script with command line

```
python src/main/python/application.py --ticker="" --api_key="" --filename="" --directory=""
```

## Running the tests

```
pytest src/main/python/tests
```

## Built With

* [pandas](https://pandas.pydata.org/docs/) - For data manipulation
* [requests](https://requests.readthedocs.io/en/master/) - To communicate with API
* [openpyxl](https://openpyxl.readthedocs.io/en/stable/) - Used to generate Excel files


## Authors

* **Jakub Pluta** - [github](https://github.com/JakubPluta)


