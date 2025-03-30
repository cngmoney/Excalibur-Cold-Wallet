import json
import time
import uuid
from pathlib import Path

INVOICE_STORAGE_FILE = Path("data/invoices.json")

class InvoiceManager:
    def __init__(self):
        self.invoices = self.load_invoices()

    def load_invoices(self):
        if INVOICE_STORAGE_FILE.exists():
            try:
                with open(INVOICE_STORAGE_FILE, 'r') as f:
                    return json.load(f)
            except Exception:
                return {}
        return {}

    def save_invoices(self):
        with open(INVOICE_STORAGE_FILE, 'w') as f:
            json.dump(self.invoices, f, indent=4)

    def create_invoice(self, sender_name, sender_address, recipient_name, recipient_address,
                       amount, currency, description=""):
        invoice_id = str(uuid.uuid4())
        timestamp = int(time.time())
        invoice = {
            "invoice_id": invoice_id,
            "timestamp": timestamp,
            "sender_name": sender_name,
            "sender_address": sender_address,
            "recipient_name": recipient_name,
            "recipient_address": recipient_address,
            "amount": amount,
            "currency": currency,
            "description": description,
            "status": "unpaid"
        }
        self.invoices[invoice_id] = invoice
        self.save_invoices()
        return invoice

    def get_invoice(self, invoice_id):
        return self.invoices.get(invoice_id)

    def mark_as_paid(self, invoice_id):
        if invoice_id in self.invoices:
            self.invoices[invoice_id]["status"] = "paid"
            self.invoices[invoice_id]["paid_timestamp"] = int(time.time())
            self.save_invoices()
            return True
        return False

    def list_invoices(self, filter_status=None):
        if filter_status:
            return {k: v for k, v in self.invoices.items() if v["status"] == filter_status}
        return self.invoices

# Example usage:
if __name__ == "__main__":
    im = InvoiceManager()
    inv = im.create_invoice(
        sender_name="Mesa Fab Inc.",
        sender_address="0xSenderAddress",
        recipient_name="Client A",
        recipient_address="0xRecipientAddress",
        amount=500.00,
        currency="RLUSD",
        description="Custom steel fabrication"
    )
    print("Created Invoice:", inv)
    print("Mark as Paid:", im.mark_as_paid(inv["invoice_id"]))
    print("All Invoices:", im.list_invoices())
