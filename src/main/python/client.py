import logging
import requests
from requests import HTTPError

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


class FMPApiClient:
    """Financial Modeling Prep api wrapper, to fetch some basic information about stock
    like company overview, financial statements and some metrics and quotations
    """

    URL = "https://financialmodelingprep.com/api/v3/"

    def __init__(self, api_key, user_name="default"):
        self._api_key = api_key
        self._user_name = user_name

    def __call_api(self, symbol, endpoint):
        """Basic method to call api endpoints
        :param symbol: tikcer symbol e.g "MMM"
        :param endpoint: api endpoint - > list of endpoints available with method show_endpoints()
        :return: response from api loaded into json file
        """

        headers = {"Content-type": "application/json"}
        response = requests.request(
            "GET",
            self.URL + f"/{endpoint}/{symbol}" + f"?apikey={self._api_key}",
            headers=headers,
        )
        validate_http_status(response)
        return  response.content #json.loads(response.content)

    @staticmethod
    def show_endpoints():
        """Display all available endpoints"""
        pass

    def fetch_company(self, symbol):
        """Fetch basic information about company"""
        return self.__call_api(symbol, ENDPOINTS_DICT["profile"])

    def fetch_balance_sheet_statement(self, symbol):
        """Fetch balance sheet statement"""
        return self.__call_api(symbol, ENDPOINTS_DICT["balance-sheet-statement"])

    def fetch_income_statement(self, symbol):
        """Fetch income statement"""
        return self.__call_api(symbol, ENDPOINTS_DICT["income-statement"])

    def fetch_cash_flow_statement(self, symbol):
        """Fetch cash flow statement"""
        return self.__call_api(symbol, ENDPOINTS_DICT["cash-flow-statement"])

    def fetch_financial_statement_as_reported(self, symbol):
        """Fetch financial statement report"""
        return self.__call_api(
            symbol, ENDPOINTS_DICT["financial-statement-full-as-reported"]
        )

    def fetch_key_metrics(self, symbol):
        """Fetch key metrics about company stock"""
        return self.__call_api(symbol, ENDPOINTS_DICT["key-metrics"])

    def fetch_ratings(self, symbol):
        """Fetch ratings of company from some analytical institutions"""
        return self.__call_api(symbol, ENDPOINTS_DICT["rating"])

    def fetch_dcf(self, symbol):
        """Fetch Discounted Cash Flow for given company"""
        return self.__call_api(symbol, ENDPOINTS_DICT["discounted-cash-flow"])

    def fetch_financial_growth(self, symbol):
        """Fetch financial growth of company"""
        return self.__call_api(symbol, ENDPOINTS_DICT["financial-growth"])

    def fetch_quote(self, symbol):
        """Fetch quotation of company"""
        return self.__call_api(symbol, ENDPOINTS_DICT["quote"])

    def fetch_ratios(self, symbol):
        """Fetch financial ratios of company"""
        return self.__call_api(symbol, ENDPOINTS_DICT["ratios"])

    def fetch_enterprise_value(self, symbol):
        """Fetch Enterprise Value of company"""
        return self.__call_api(symbol, ENDPOINTS_DICT["enterprise-value"])
