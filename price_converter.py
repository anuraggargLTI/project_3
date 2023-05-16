import pandas as pd
import os
from dotenv import load_dotenv
import requests
import json
request_url = "https://api.coinbase.com/v2/exchange-rates?currency=ETH"
def getETHPrice(dollar_price):
    response = requests.get(request_url).json()
    return float(dollar_price)/float(response["data"]["rates"]["USD"])