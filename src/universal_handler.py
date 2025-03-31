from exchange_manager import ExchangeManager
from fiat_conversion import FiatConversion
from ledger_system import LedgerSystem
from invoice_manager import InvoiceManager
from transaction_manager import TransactionManager
from settings_manager import SettingsManager
from storage_handler import StorageHandler

class UniversalHandler:
    def __init__(self):
        self.wallet = WalletAPI()
        self.exchange = ExchangeManager()
        self.fiat = FiatConversion()
        self.ledger = LedgerSystem()
        self.invoice = InvoiceManager()
        self.tx = TransactionManager()
        self.settings = SettingsManager()
        self.storage = StorageHandler()

    def swap_crypto(self, wallet, from_currency, to_currency, amount):
        result = self.exchange.simulate_swap(wallet, from_currency, to_currency, amount)
        self.ledger.add_entry(
            entry_type="swap",
            currency=from_currency,
            amount=amount,
            description=f"Swapped {amount} {from_currency} to {to_currency}"
        )
        return result

    def convert_fiat(self, amount, from_fiat, to_fiat):
        return self.fiat.convert(amount, from_fiat, to_fiat)

    def create_and_send_invoice(self, sender_info, recipient_info, amount, currency, description=""):
        invoice = self.invoice.create_invoice(
            sender_info["name"], sender_info["address"],
            recipient_info["name"], recipient_info["address"],
            amount, currency, description
        )
        return invoice

    def mark_invoice_paid_and_log(self, invoice_id):
        invoice = self.invoice.get_invoice(invoice_id)
        if invoice and invoice['status'] == 'unpaid':
            self.invoice.mark_as_paid(invoice_id)
            self.ledger.add_entry(
                entry_type="invoice_payment",
                currency=invoice['currency'],
                amount=invoice['amount'],
                description=f"Invoice {invoice_id} paid",
                invoice_id=invoice_id
            )
            return True
        return False

    def send_transaction(self, wallet, to_address, amount, currency, description=""):
        return self.tx.send_funds(wallet, to_address, amount, currency, description)

    def receive_transaction(self, wallet, from_address, amount, currency, description=""):
        return self.tx.receive_funds(wallet, from_address, amount, currency, description)

# Example usage:
if __name__ == "__main__":
    uh = UniversalHandler()
    wallet = {"address": "0xME", "BTC": 1.0, "ETH": 0.0}
    print(uh.swap_crypto(wallet, "BTC", "ETH", 0.5))
