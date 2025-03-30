# crypto_processor.py

import hashlib
import time

class CryptoProcessor:
    def __init__(self):
        self.transaction_history = []

    def generate_transaction_id(self, sender, receiver, amount, timestamp=None):
        timestamp = timestamp or str(time.time())
        data = f"{sender}-{receiver}-{amount}-{timestamp}"
        return hashlib.sha256(data.encode()).hexdigest()

    def validate_transaction(self, sender_balance, amount):
        if amount <= 0:
            print("[ERROR] Transaction amount must be greater than zero.")
            return False
        if sender_balance < amount:
            print("[ERROR] Insufficient balance.")
            return False
        return True

    def process_transaction(self, sender, receiver, amount, sender_balance):
        if not self.validate_transaction(sender_balance, amount):
            return None

        tx_id = self.generate_transaction_id(sender, receiver, amount)
        transaction = {
            "tx_id": tx_id,
            "sender": sender,
            "receiver": receiver,
            "amount": amount,
            "timestamp": time.time()
        }

        self.transaction_history.append(transaction)
        print(f"[SUCCESS] Transaction processed: {tx_id}")
        return transaction

    def get_transaction_history(self):
        return self.transaction_history
