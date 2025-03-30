import json
from decimal import Decimal, ROUND_DOWN
from pathlib import Path

# Fiat conversion will depend on real-time or cached rates
FIAT_RATES_FILE = Path("data/fiat_rates.json")

# Default conversion rates to USD
DEFAULT_FIAT_RATES = {
    "USD": 1.0,
    "EUR": 0.91,
    "GBP": 0.78,
    "JPY": 151.20,
    "CAD": 1.35,
    "AUD": 1.52,
    "CHF": 0.91
}

class FiatConversion:
    def __init__(self):
        self.rates = self.load_fiat_rates()

    def load_fiat_rates(self):
        if FIAT_RATES_FILE.exists():
            try:
                with open(FIAT_RATES_FILE, 'r') as f:
                    return json.load(f)
            except Exception:
                return DEFAULT_FIAT_RATES
        else:
            return DEFAULT_FIAT_RATES

    def save_fiat_rates(self):
        with open(FIAT_RATES_FILE, 'w') as f:
            json.dump(self.rates, f, indent=4)

    def update_rate(self, from_fiat: str, to_fiat: str, rate: float):
        self.rates[from_fiat.upper()] = rate
        self.save_fiat_rates()

    def convert(self, amount: float, from_fiat: str, to_fiat: str) -> float:
        from_fiat = from_fiat.upper()
        to_fiat = to_fiat.upper()

        if from_fiat == to_fiat:
            return amount

        try:
            usd_amount = Decimal(str(amount)) / Decimal(str(self.rates[from_fiat]))
            target_amount = usd_amount * Decimal(str(self.rates[to_fiat]))
            return float(target_amount.quantize(Decimal('0.01'), rounding=ROUND_DOWN))
        except KeyError:
            raise ValueError(f"Conversion rate from {from_fiat} to {to_fiat} not available.")

# Example usage:
if __name__ == "__main__":
    fc = FiatConversion()
    print("USD to EUR:", fc.convert(100, "USD", "EUR"))
    print("JPY to GBP:", fc.convert(10000, "JPY", "GBP"))
