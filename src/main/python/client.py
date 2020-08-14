import logging
import requests
from requests import HTTPError
from settings.default import TOKEN


ENDPOINTS = {
    "Company Profile" : "stock/profile2",
    "Stock Symbol" : "/stock/symbol?exchange=US",
    "Company News" : "/company-news",
    "News Sentiment" : "/news-sentiment",
    "Basic Financials" : "/stock/metric",
    "Financials As Reported" : "/stock/financials-reported",
    "SEC Filings" : "/stock/filings",
    "Recommendation Trends" : "/stock/recommendation",
    "Quote" : "/quote"

}


logging.basicConfig(level="INFO")
logger = logging.getLogger(__name__)


def validate_http_status(response) -> None:
    """
    Validate if Request Status = 200 else Raise an Exception.
    """
    status_code = response.status_code
    message = response.text

    if response.status_code != 200:
        raise HTTPError(message)
    logger.debug("Request Successful: {}".format(status_code))


class FinnhubClient:
    """Finnhub api wrapper, to fetch financial data
    """

    URL = 'https://finnhub.io/api/v1/'

    def __init__(self, api_key, user_name="default"):
        self._api_key = api_key
        self._user_name = user_name

    def __call_api(self, symbol, endpoint):
        """Basic method to call api endpoints
        :param symbol: tikcer symbol e.g "MMM"
        :param endpoint: api endpoint - > list of endpoints available with method show_endpoints()
        :return: response from api loaded into json file
        """
        headers = {"Content-type": "application/json",
                   "X-Finnhub-Token": TOKEN}

        response = requests.get(self.URL + f"/{endpoint}?symbol={symbol}", headers=headers)
        validate_http_status(response)
        return response.json()

    @staticmethod
    def show_endpoints():
        """Display all available endpoints"""
        print(ENDPOINTS.keys())

    def fetch_company(self, symbol):
        """Fetch basic information about company"""
        return self.__call_api(symbol, ENDPOINTS["Company Profile"])


    def fetch_financial_statement_as_reported(self, symbol):
        """Fetch financial statement report"""
        return self.__call_api(
            symbol, ENDPOINTS["Financials As Reported"]
        )

    def fetch_key_metrics(self, symbol):
        """Fetch key metrics about company stock"""
        return self.__call_api(symbol, ENDPOINTS["Basic Financials"])

    def fetch_company_news(self, symbol):
        """Fetch company news"""
        return self.__call_api(symbol, ENDPOINTS["Company News"])

    def fetch_news_sentiments(self, symbol):
        """Fetch company news sentiments"""
        return self.__call_api(symbol, ENDPOINTS["News Sentiment"])

    def fetch_quote(self, symbol):
        """Fetch quotation of company"""
        return self.__call_api(symbol, ENDPOINTS["Quote"])

    def fetch_recommendations(self, symbol):
        """Fetch recommendations"""
        return self.__call_api(symbol, ENDPOINTS["Recommendation Trends"])

    def fetch_sec_fillings(self, symbol):
        """Fetch SEC Filings"""
        return self.__call_api(symbol, ENDPOINTS["SEC Filings"])
