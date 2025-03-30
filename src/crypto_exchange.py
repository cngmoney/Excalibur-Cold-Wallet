# crypto_exchange.py

import requests
import time

class CryptoExchange:
    def __init__(self):
        self.api_url = "https://api.coingecko.com/api/v3/simple/price"
        self.supported_coins = ["bitcoin", "ethereum", "litecoin"]
        self.vs_currencies = ["usd", "btc", "eth"]
        self.last_rates = {}

    def fetch_exchange_rates(self):
        try:
            params = {
                "ids": ",".join(self.supported_coins),
                "vs_currencies": ",".join(self.vs_currencies)
            }
            response = requests.get(self.api_url, params=params)
            if response.status_code == 200:
                self.last_rates = response.json()
                return self.last_rates
            else:
                print(f"[ERROR] Failed to fetch exchange rates: {response.status_code}")
                return None
        except Exception as e:
            print(f"[EXCEPTION] Exchange API failed: {e}")
            return None

    def convert(self, amount, from_coin, to_coin):
        from_coin = from_coin.lower()
        to_coin = to_coin.lower()

        if not self.last_rates:
            self.fetch_exchange_rates()

        try:
            if from_coin == to_coin:
                return amount

            if from_coin not in self.last_rates or to_coin not in self.vs_currencies:
                print(f"[ERROR] Unsupported conversion: {from_coin} to {to_coin}")
                return None

            rate = self.last_rates[from_coin][to_coin]
            return round(amount * rate, 8)

        except Exception as e:
            print(f"[EXCEPTION] Conversion failed: {e}")
            return None
