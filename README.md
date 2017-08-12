# satoshi
A simple command line satoshi to fiat currency conversion tool.


Satoshi.py is a simple command line conversion tool for satoshis to fiat currency (USD, EUR, CNY, etc.).

This script uses the CryptoCompare API to get the rates of various cryptocurrencies.  https://www.cryptocompare.com/api/

## Dependencies

This script uses the urllib3 and certifi python libraries.  Therefore, you must install them first before using this script.  Also, you will need to install pip in order to install those libraries.  If you do not have pip installed, check out this link for more information on how to do that: https://pip.pypa.io/en/stable/installing/  

Once you have pip installed, enter the following commands at the command line to install urllib3 and certifi:

    pip install urllib3[secure]
    pip install certifi


## Usage

To use it, you must provide an amount of satoshis, one cryptocurrency symbol of the satoshis (BTC, LTC, etc.), and desired fiat currency for each of the tags -s, -c, and -f [respectively].  For example:

    python satoshi.py -s 25640 -c BTC -f USD

The cryptocurrency and fiat symbols can be either lowercase or uppercase.

You can list multiple unique fiat currency symbols, separated by a comma.  For example:

    python satoshi.py -s 25640 -c BTC -f USD,EUR,JPY,CNY,CAD

The script will print to standard output the fiat currencies and value of satoshis, as a tab delimited pair, one per line.
