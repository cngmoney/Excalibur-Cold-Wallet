import json
import time
from pathlib import Path

LEDGER_FILE = Path("data/ledger.json")

class LedgerSystem:
    def __init__(self):
        self.ledger = self.load_ledger()

    def load_ledger(self):
        if LEDGER_FILE.exists():
            try:
                with open(LEDGER_FILE, 'r') as f:
                    return json.load(f)
            except Exception:
                return []
        return []

    def save_ledger(self):
        with open(LEDGER_FILE, 'w') as f:
            json.dump(self.ledger, f, indent=4)

    def add_entry(self, entry_type, currency, amount, description="", tx_hash=None, invoice_id=None):
        entry = {
            "timestamp": int(time.time()),
            "entry_type": entry_type,  # e.g., 'credit', 'debit', 'swap', 'invoice_payment'
            "currency": currency,
            "amount": amount,
            "description": description,
            "tx_hash": tx_hash,
            "invoice_id": invoice_id
        }
        self.ledger.append(entry)
        self.save_ledger()
        return entry

    def get_all_entries(self):
        return self.ledger

    def filter_entries(self, entry_type=None, currency=None):
        filtered = self.ledger
        if entry_type:
            filtered = [e for e in filtered if e["entry_type"] == entry_type]
        if currency:
            filtered = [e for e in filtered if e["currency"] == currency]
        return filtered

# Example usage:
if __name__ == "__main__":
    ledger = LedgerSystem()
    ledger.add_entry("invoice_payment", "RLUSD", 500, "Paid Invoice #12345", invoice_id="12345")
    print("All Ledger Entries:")
    for entry in ledger.get_all_entries():
        print(entry)
