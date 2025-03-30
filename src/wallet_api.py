import json
import os
from pathlib import Path
from hashlib import sha256
from storage_handler import StorageHandler

WALLET_FILE = "wallet_data.enc"

class WalletAPI:
    def __init__(self):
        self.storage = StorageHandler()
        self.wallet = self.load_wallet()

    def load_wallet(self):
        data = self.storage.load_and_decrypt(WALLET_FILE)
        if data is None:
            print("🚨 No wallet found. Creating new one...")
            return self.create_new_wallet()
        return data

    def create_new_wallet(self):
        address = self.generate_address()
        wallet = {
            "address": address,
            "balances": {
                "BTC": 0.0,
                "ETH": 0.0,
                "RLUSD": 0.0,
                "EXC": 0.0
            }
        }
        self.save_wallet(wallet)
        return wallet

    def generate_address(self):
        seed = os.urandom(32)
        address = sha256(seed).hexdigest()
        return f"0x{address[:40]}"

    def save_wallet(self, wallet):
        self.storage.encrypt_and_store(WALLET_FILE, wallet)

    def get_balance(self, currency):
        return self.wallet["balances"].get(currency.upper(), 0.0)

    def update_balance(self, currency, amount):
        currency = currency.upper()
        self.wallet["balances"][currency] = amount
        self.save_wallet(self.wallet)

    def get_address(self):
        return self.wallet["address"]

# Example usage:
if __name__ == "__main__":
    api = WalletAPI()
    print("Address:", api.get_address())
    print("BTC Balance:", api.get_balance("BTC"))
    api.update_balance("BTC", 1.5)
    print("Updated BTC Balance:", api.get_balance("BTC"))
