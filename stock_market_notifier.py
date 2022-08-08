import yfinance
from config import stocks
import pandas as pd
from datetime import datetime
from datetime import timedelta


# NOTE: This package uses the financial data from yahoo which refers to the American stock market.

def main():

    # get start and end time
    current_time = datetime.now()

    # strip off seconds and go back one minute to make sure that data is already available
    current_time = current_time.replace(second=0, microsecond=0)

    # Download data for last three days
    # In case there are multiple holidays, or holidays after a week-end, otherwise
    # the download command for only one day could fail as there is no new data published
    # during weekends or holidays.
    start_time = current_time - timedelta(days=3)

    # get USD to EUR exchange rate
    exchange_data = yfinance.download(tickers="EUR=X", progress=False, start=start_time,
                                      end=current_time, interval='1m')
    exchange_price_usd_to_eur = exchange_data.tail(1)["Close"][0]

    # get actual prices for stocks in EUR
    stock_list = [s for s in stocks]
    data = yfinance.download(tickers=stock_list, progress=False, start=start_time,
                             end=current_time, interval='1m')

    result = []
    df = pd.DataFrame.from_dict(data)  # contains dataframe for all companies with all values
    df.dropna(axis='index', inplace=True) # drop all NaN values

    close_prices = df.tail(1)["Close"] # get last row that wasn't NaN

    for company in close_prices.iteritems():
        time = company[1].index[0]
        time = datetime.fromisoformat(str(time))
        time = time.replace(hour=time.hour+6) #shift to UTC+1 time
        timestr = time.strftime("%d.%m.%Y %H:%M")

        usd_price = company[1][0]
        eur_price = usd_price * exchange_price_usd_to_eur

        if eur_price > stocks[company[0]]["price_limit"] or pd.isna(eur_price):
            result.append((stocks[company[0]]["description"], str(round(eur_price, 2)) + " €", timestr))
    return result


main()
