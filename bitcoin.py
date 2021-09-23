# bitcoin.py
# This program outputs all the price in the three currencies
# Author: Fatima Zeino

import requests
url="https://api.coindesk.com/v1/bpi/currentprice.json"
returnedData=requests.get(url)
bitcoindict=returnedData.json()
#print(bitcoindict)
for item in bitcoindict["bpi"]:
 print ("Today bitcoin price in {} is {} ".format(bitcoindict["bpi"][item]["code"], bitcoindict["bpi"][item]["rate"]))


''' {"time":
{"updated":"Feb 14, 2021 00:16:00 UTC","updatedISO":"2021-02-14T00:16:00+00:00","updateduk":"Feb 14, 2021 at 00:16 GMT"
},
"disclaimer":"This data was produced from the CoinDesk Bitcoin Price Index (USD). Non-USD currency data converted using hourly conversion rate from openexchangerates.org","chartName":"Bitcoin",
"bpi":
{"USD":
{"code":"USD","symbol":"&#36;","rate":"47,627.3615","description":"United States Dollar","rate_float":47627.3615},
"GBP":
{"code":"GBP","symbol":"&pound;","rate":"34,407.8634","description":"British Pound Sterling","rate_float":34407.8634}
,"EUR"
{"code":"EUR","symbol":"&euro;","rate":"39,294.9070","description":"Euro","rate_float":39294.907}
}
} '''