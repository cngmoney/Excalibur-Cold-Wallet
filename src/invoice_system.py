from invoice_manager import InvoiceManager
import time

class InvoiceSystem:
    def __init__(self):
        self.manager = InvoiceManager()

    def generate_invoice(self):
        print("\n--- Create New Invoice ---")
        sender_name = input("Sender Name: ")
        sender_address = input("Sender Wallet Address: ")
        recipient_name = input("Recipient Name: ")
        recipient_address = input("Recipient Wallet Address: ")
        amount = float(input("Amount: "))
        currency = input("Currency (e.g., RLUSD, EXC, BTC): ").upper()
        description = input("Description (optional): ")

        invoice = self.manager.create_invoice(
            sender_name, sender_address,
            recipient_name, recipient_address,
            amount, currency, description
        )

        print("\n✅ Invoice Created:")
        self.display_invoice(invoice)

    def display_invoice(self, invoice):
        print("-----------------------------")
        print(f"Invoice ID: {invoice['invoice_id']}")
        print(f"Timestamp: {time.ctime(invoice['timestamp'])}")
        print(f"From: {invoice['sender_name']} ({invoice['sender_address']})")
        print(f"To: {invoice['recipient_name']} ({invoice['recipient_address']})")
        print(f"Amount: {invoice['amount']} {invoice['currency']}")
        print(f"Description: {invoice['description']}")
        print(f"Status: {invoice['status']}")
        if invoice['status'] == 'paid':
            print(f"Paid Timestamp: {time.ctime(invoice['paid_timestamp'])}")
        print("-----------------------------")

    def list_invoices(self):
        print("\n--- All Invoices ---")
        all_invoices = self.manager.list_invoices()
        for invoice in all_invoices.values():
            self.display_invoice(invoice)

    def mark_invoice_paid(self):
        invoice_id = input("\nEnter Invoice ID to Mark as Paid: ")
        success = self.manager.mark_as_paid(invoice_id)
        if success:
            print("✅ Invoice marked as paid.")
        else:
            print("❌ Invoice ID not found.")

if __name__ == "__main__":
    system = InvoiceSystem()
    
    while True:
        print("\n=== Invoice System Menu ===")
        print("1. Create New Invoice")
        print("2. List All Invoices")
        print("3. Mark Invoice as Paid")
        print("4. Exit")

        choice = input("Select an option (1-4): ")

        if choice == "1":
            system.generate_invoice()
        elif choice == "2":
            system.list_invoices()
        elif choice == "3":
            system.mark_invoice_paid()
        elif choice == "4":
            print("Goodbye.")
            break
        else:
            print("Invalid choice. Try again.")
