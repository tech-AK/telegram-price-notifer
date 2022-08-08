from config import *
import requests
from datetime import datetime

def get_newest_prices(retry=0):
    current_time = datetime.utcnow()

    try:
        import crypto_notifier
        results_coin = crypto_notifier.main()

        hour = current_time.strftime("%H")
        # USA stock market is open between 14.00 - 21:00 (UTC+0) on weekdays.
        # Yahoo Finance sends data from 14.30 - 21.00 (UTC+0) on weekdays.
        # So this script can terminate if it is weekend or outside the time window.
        if ('15' <= hour <= '21') and (0 <= current_time.weekday() <= 4):
            import stock_market_notifier
            results_stock = stock_market_notifier.main()
            results = [*results_coin, *results_stock]
        else:
            results = results_coin

        for (name, price, timestr) in results:
            notify_user(f" !!! New Price Alert at {timestr} !!! \n{name} – {price}")
    except:
        if retry >= 10:
            timestr = current_time.strftime("%H:%M")
            notify_user(f"Error at {timestr} (UTC+0). Exception raised.")
        else:
            print("Exception raised. Retry Nr.:", retry)
            get_newest_prices(retry + 1)


def notify_user(msg):
    for chat_id in allowed_IDs:

        try:
            params = {"chat_id": chat_id, "text": msg}
            url = f"https://api.telegram.org/bot{token}/sendMessage"
            request_status = requests.post(url, params=params)
            logging.info(f"Message is send to ID {chat_id}. Status: {request_status.status_code}. Content:\n{msg}\n")
        except:
            logging.error(f"Message COULD NOT BE sent to ID {chat_id}. Content:\n{msg}\n")


if __name__ == "__main__":
    get_newest_prices()