#! /usr/bin/python
# A simple utility that will calculate bitcoin balance from an electrum wallet.
# Requires: electrum
# Assumes: you currently have bitcoin stored in an electrum wallet.
# Author: William Bradley
# BunsenLabs Forum Handle: tknomanzr
# License: wtfpl. Use this script however you see fit.
import json, urllib2, subprocess
url = 'https://coinbase.com/api/v1/prices/historical'
# Get current bitcoin price
price =  urllib2.urlopen(url)
price_data = price.read(33)
price_data = price_data[26:-2]
price_data = float(price_data)
# Get balance from wallet.
# It comes in as a json object that needs to be converted.
#balance = json.loads(subprocess.check_output(["electrum","getbalance"]))
#current_balance = balance['confirmed']
#current_balance = float(current_balance)
# Get approximate value of bitcoin in wallet.
value = price_data
print str(price_data)    
