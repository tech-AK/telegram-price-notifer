# Stock Market and Crypto Market Telegram Notifier 

## Purpose / Motivation
This is a small bot for telegram to keep track of the current stock market and crypto market prices. It checks the price of pre-selected assets and if the price is higher than the pre-selected limit price, it notifies the user. 

## How to use
Use ``crontab`` on a server to start the ``main.py`` regularly (e. g. every hour). The ``config.py`` can be used to configure your ``BOT_TOKEN`` and the assets this program should observe. 
Note: This project is more or less a prototype and not broadly configurable, e. g. it always uses EUR as currency and reports the time in timezone UTC+1.

## Run
1. First install dependencies: ``pip install -r requirements.txt``
2. Run program regularly (e. g. via crontab): ``py main.py``