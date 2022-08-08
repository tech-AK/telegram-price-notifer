import logging
import sys

allowed_IDs = [] #insert the IDs of all telegram participants who should be notfied
token = '' #INSERT SECRET BOT TOKEN

# Source: Binance
coins = {
    "ETHEUR": {"description": "Ethereum", "price_limit": 2000},
    "BTCEUR": {"description": "Bitcoin", "price_limit": 10000}
         }

# Source: Yahoo Finance
# find out the 'ticker' names like GOOG by using Yahoo Finance
stocks = {
    "GOOG": {"description": "Google", "price_limit": 100},
    "NVAX": {"description": "Novavax", "price_limit": 50}
         }

logging.basicConfig(filename='../bot_notifier.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(sys.stdout)) #also enable info logging to console