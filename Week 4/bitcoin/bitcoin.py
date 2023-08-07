import requests
import json
import sys


def main():
    # argument error handling
    if len(sys.argv) < 2:
        #get_bitcoin_price(1) #For debug purposes only
        sys.exit("Missing command-line argument")
    elif len(sys.argv) == 2:
        try:
            float(sys.argv[1])
        except ValueError:
            sys.exit("Command-line argument is not a number")

    get_bitcoin_price(sys.argv[1])


def get_bitcoin_price(num_coins):
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    headers = {"accept": "application/json"}

    # Try and get data from CoinDesk API
    try:
        response = requests.get(url, headers=headers).json()
    except requests.RequestException:
        sys.exit("Unable to retrieve current data from CoinDesk API")
    else:
        usd_rate_float = response['bpi']['USD']['rate_float']
        amount = float(num_coins) * float(usd_rate_float)
        print(f"${amount:,.4f}")


if __name__ == "__main__":
    main()