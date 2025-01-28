import json
import requests
import sys

if len(sys.argv)<2:
    sys.exit("Missing command-line argument")
elif (isinstance(sys.argv[1],float) or isinstance(sys.argv[1],int))!=1:
    sys.exit("Command-line is not a number")
try:
    response=requests.get("https://api.coindesk.com/v1/bpi/currentprice.json" )
    # print(json.dumps(response.json(),indent=2))
    price=(response.json()["bpi"]["USD"]['rate_float'])
    amount=float(sys.argv[1])*price
    print(f"${amount:,.4f}")
except requests.RequestException:
    sys.exit()
