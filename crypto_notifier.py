import json
from config import coins
import requests
from datetime import datetime

from requests.adapters import HTTPAdapter

from requests.adapters import Retry


def main():
    # Handle retries
    session = requests.Session()
    retries = Retry(total=500,  # total no auf retries
                       backoff_factor=0.4,  # wait backoff_factor * (2*no.retry - 1) seconds between retry
                       status_forcelist=[500, 502, 503, 504])  # retry for every scenario

    session.mount('https://', HTTPAdapter(max_retries=retries))

    result = []
    for coinID, coin_details in coins.items():
        response = session.get(f'https://api.binance.com/api/v3/ticker/price?symbol={coinID}')

        if response.status_code != requests.codes.ok:
            print("Something went wrong at fetching data from Binance")
        else:
            timestr = datetime.now().strftime("%H:%M")
            # Get data
            data = json.loads(response.text)
            price = float(data["price"])
            if price > coin_details["price_limit"]:
                result.append((coin_details["description"], str(round(price, 2)) + " €", timestr))

    return result
