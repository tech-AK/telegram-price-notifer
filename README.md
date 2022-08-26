# Stock Market and Crypto Market Telegram Notifier 

## Purpose / Motivation
This is a small bot for telegram to keep track of the current stock market and crypto market prices. It checks the price of pre-selected assets and if the price is higher than the pre-selected limit price, it notifies the user. 

## How to use
Use ``crontab`` on a server to start the ``main.py`` regularly (e. g. every hour). The ``config.py`` can be used to configure your ``BOT_TOKEN`` and the assets which this program should observe.

## Run
1. First install dependencies: ``pip install -r requirements.txt``
2. Run program regularly (e. g. via crontab): ``py main.py``
