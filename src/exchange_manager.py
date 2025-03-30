import json
import time
from decimal import Decimal, ROUND_DOWN
from pathlib import Path

# Simulated rates for offline exchange - future: sync with API when online
EXCHANGE_RATES_FILE = Path("data/exchange_rates.json")

# Default rates (used if no cache exists)
DEFAULT_RATES = {
    "BTC": {"USD": 65000, "EXC": 1300000, "ETH": 20},
    "ETH": {"USD": 3300, "BTC": 0.05, "EXC": 70000},
    "EXC": {"USD": 0.50, "BTC": 0.00000077, "ETH": 0.000014},
    "RLUSD": {"USD": 1.0}
}

class ExchangeManager:
    def __init__(self):
        self.rates = self.load_exchange_rates()

    def load_exchange_rates(self):
        if EXCHANGE_RATES_FILE.exists():
            try:
                with open(EXCHANGE_RATES_FILE, 'r') as f:
                    return json.load(f)
            except Exception:
                return DEFAULT_RATES
        else:
            return DEFAULT_RATES

    def save_exchange_rates(self):
        with open(EXCHANGE_RATES_FILE, 'w') as f:
            json.dump(self.rates, f, indent=4)

    def convert(self, amount: float, from_currency: str, to_currency: str) -> float:
        if from_currency == to_currency:
            return amount

        try:
            rate = self.rates[from_currency][to_currency]
            converted = Decimal(str(amount)) * Decimal(str(rate))
            return float(converted.quantize(Decimal('0.00000001'), rounding=ROUND_DOWN))
        except KeyError:
            raise ValueError(f"Exchange rate from {from_currency} to {to_currency} not available.")

    def update_rate(self, from_currency: str, to_currency: str, rate: float):
        if from_currency not in self.rates:
            self.rates[from_currency] = {}
        self.rates[from_currency][to_currency] = rate
        self.save_exchange_rates()

    def list_supported_pairs(self):
        return [(f, t) for f in self.rates for t in self.rates[f]]

    def simulate_swap(self, wallet: dict, from_currency: str, to_currency: str, amount: float):
        if wallet.get(from_currency, 0) < amount:
            raise ValueError(f"Insufficient balance in {from_currency}.")

        received = self.convert(amount, from_currency, to_currency)
        wallet[from_currency] -= amount
        wallet[to_currency] = wallet.get(to_currency, 0) + received

        return {
            "timestamp": int(time.time()),
            "from": from_currency,
            "to": to_currency,
            "amount_sent": amount,
            "amount_received": received
        }

# Example usage (to be replaced with integration into full wallet system):
if __name__ == "__main__":
    em = ExchangeManager()
    print("Supported Pairs:", em.list_supported_pairs())
    result = em.simulate_swap({"BTC": 0.01, "ETH": 0}, "BTC", "ETH", 0.005)
    print("Swap Result:", result)
