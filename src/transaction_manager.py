import time
import hashlib
import json

from ledger_system import LedgerSystem
from storage_handler import StorageHandler

class TransactionManager:
    def __init__(self):
        self.ledger = LedgerSystem()
        self.storage = StorageHandler()

    def generate_tx_hash(self, sender, recipient, amount, currency):
        raw = f"{sender}{recipient}{amount}{currency}{time.time()}"
        return hashlib.sha256(raw.encode()).hexdigest()

    def send_funds(self, sender_wallet, recipient_address, amount, currency, description=""):
        if sender_wallet.get(currency, 0) < amount:
            print("❌ Insufficient balance.")
            return None

        # Deduct funds and simulate transaction
        sender_wallet[currency] -= amount
        tx_hash = self.generate_tx_hash(sender_wallet.get("address", "unknown"), recipient_address, amount, currency)

        # Log to ledger
        entry = self.ledger.add_entry(
            entry_type="send",
            currency=currency,
            amount=amount,
            description=description or f"Sent to {recipient_address}",
            tx_hash=tx_hash
        )

        print(f"✅ Transaction complete. TX Hash: {tx_hash}")
        return entry

    def receive_funds(self, recipient_wallet, sender_address, amount, currency, description=""):
        recipient_wallet[currency] = recipient_wallet.get(currency, 0) + amount
        tx_hash = self.generate_tx_hash(sender_address, recipient_wallet.get("address", "unknown"), amount, currency)

        entry = self.ledger.add_entry(
            entry_type="receive",
            currency=currency,
            amount=amount,
            description=description or f"Received from {sender_address}",
            tx_hash=tx_hash
        )

        print(f"📥 Funds received. TX Hash: {tx_hash}")
        return entry

# Example usage:
if __name__ == "__main__":
    tm = TransactionManager()
    wallet = {"address": "0xMYADDRESS", "RLUSD": 100.0}
    tm.send_funds(wallet, "0xRECIPIENT", 25.0, "RLUSD")
    tm.receive_funds(wallet, "0xSENDER", 40.0, "RLUSD")
