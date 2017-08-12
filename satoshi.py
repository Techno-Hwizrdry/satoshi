#!/usr/bin/env python

__author__  = "Alexan Mardigian"
__version__ = "0.0.1"

from argparse import ArgumentParser

import certifi
import json
import sys
import urllib3

API_URL      = "https://min-api.cryptocompare.com/data/price?fsym=%s&tsyms=%s"
COINFRACTION = float(10**-8)    # A satoshi is one hundred millionth (0.00000001) of 1 coin.

class SatoshiParser(ArgumentParser):
	def error(self, message):
		sys.stderr.write('error: %s\n' %message)
		self.print_help()
		sys.exit(2)

def get_args():
	parser = SatoshiParser()

	parser.add_argument('-s', dest='satoshis',        help='Amount of satoshis you wish to convert to fiat currency.')
	parser.add_argument('-c', dest='crypto_currency', help='Desired cryptocurrency symbol to reference.')
    	parser.add_argument('-f', dest='fiat_currency',   help='Desired fiat currency value.')

	if len(sys.argv) == 1:      # If no arguments were provided, then print help and exit.
		parser.print_help()
		sys.exit(1)

	return parser.parse_args()

#  This function will convert the amount of satoshis to it's fiat currency value.
#  It takes the fiat value of 1 crypto-coin and the amount of satoshis as parameters,
#  and returns a string that represents the fiat value of those satoshis.
def satoshi_to_fiat(coin_value, satoshis):
	fiat_value = float(satoshis * COINFRACTION) * float(coin_value)

	return '{:.2f}'.format(fiat_value)

def main():
	opts = get_args()
	http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
	url  = API_URL % (opts.crypto_currency.upper(), opts.fiat_currency.upper())

	req  = http.request('GET', url, retries=False)

	results = json.loads(req.data)  # Convert our results, a string, into a dictionary.

	for fiat_symbol, value in results.iteritems():
		print fiat_symbol + "\t" + satoshi_to_fiat(value, int(opts.satoshis))

if __name__ == '__main__':
	main()
