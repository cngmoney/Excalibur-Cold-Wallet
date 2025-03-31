from universal_handler import UniversalHandler
from user_input import UserInput


def main():
    ui = UserInput()
    uh = UniversalHandler()

    wallet = uh.storage.load_and_decrypt("wallet_data.enc")
    if not wallet:
        wallet = uh.wallet.create_new_wallet()
        uh.storage.encrypt_and_store("wallet_data.enc", wallet)
    else:
        uh.wallet.wallet = wallet

    print(f"\n🔐 Wallet Address: {uh.wallet.get_address()}")

    while True:
        print("\n=== Excalibur Cold Wallet Main Menu ===")
        print("1. View Balances")
        print("2. Send Funds")
        print("3. Receive Funds")
        print("4. Swap Crypto")
        print("5. Convert Fiat")
        print("6. Invoicing")
        print("7. Ledger History")
        print("8. Exit")

        choice = ui.prompt_choice("Choose an option", [
            "View Balances", "Send Funds", "Receive Funds",
            "Swap Crypto", "Convert Fiat", "Invoicing",
            "Ledger History", "Exit"
        ])

        if choice == "View Balances":
            print("\n💰 Wallet Balances:")
            for currency, balance in uh.wallet.wallet["balances"].items():
                print(f"  {currency}: {balance}")

        elif choice == "Send Funds":
            to_address = ui.prompt_string("Recipient Address")
            currency = ui.prompt_string("Currency (BTC, ETH, RLUSD, EXC)").upper()
            amount = ui.prompt_float("Amount", min_val=0.00000001)
            desc = ui.prompt_string("Optional Description", allow_empty=True)
            uh.send_transaction(uh.wallet.wallet["balances"], to_address, amount, currency, desc)
            uh.wallet.update_balance(currency, uh.wallet.wallet["balances"][currency])

        elif choice == "Receive Funds":
            from_address = ui.prompt_string("Sender Address")
            currency = ui.prompt_string("Currency").upper()
            amount = ui.prompt_float("Amount", min_val=0.00000001)
            desc = ui.prompt_string("Optional Description", allow_empty=True)
            uh.receive_transaction(uh.wallet.wallet["balances"], from_address, amount, currency, desc)
            uh.wallet.update_balance(currency, uh.wallet.wallet["balances"][currency])

        elif choice == "Swap Crypto":
            print("Current Wallet:", uh.wallet.wallet["balances"])
            from_currency = ui.prompt_string("From Currency").upper()
            to_currency = ui.prompt_string("To Currency").upper()
            amount = ui.prompt_float("Amount", min_val=0.00000001)
            result = uh.swap_crypto(uh.wallet.wallet["balances"], from_currency, to_currency, amount)
            uh.wallet.save_wallet(uh.wallet.wallet)
            print("✅ Swap Result:", result)

        elif choice == "Convert Fiat":
            from_fiat = ui.prompt_string("From Fiat (USD, EUR, GBP, etc.)").upper()
            to_fiat = ui.prompt_string("To Fiat").upper()
            amount = ui.prompt_float("Amount", min_val=0.01)
            result = uh.convert_fiat(amount, from_fiat, to_fiat)
            print(f"{amount} {from_fiat} = {result} {to_fiat}")

        elif choice == "Invoicing":
            sub_choice = ui.prompt_choice("Invoice Options", ["Create Invoice", "Mark Paid", "Back"])
            if sub_choice == "Create Invoice":
                sender = {"name": ui.prompt_string("Sender Name"), "address": uh.wallet.get_address()}
                recipient = {
                    "name": ui.prompt_string("Recipient Name"),
                    "address": ui.prompt_string("Recipient Wallet Address")
                }
                amount = ui.prompt_float("Amount", min_val=0.00001)
                currency = ui.prompt_string("Currency").upper()
                description = ui.prompt_string("Description", allow_empty=True)
                invoice = uh.create_and_send_invoice(sender, recipient, amount, currency, description)
                print("📄 Invoice Created:", invoice)
            elif sub_choice == "Mark Paid":
                invoice_id = ui.prompt_string("Invoice ID")
                if uh.mark_invoice_paid_and_log(invoice_id):
                    print("✅ Invoice marked as paid and logged.")
                else:
                    print("❌ Could not mark invoice. Check ID or status.")

        elif choice == "Ledger History":
            print("\n📘 Ledger Entries:")
            for entry in uh.ledger.get_all_entries():
                print(entry)

        elif choice == "Exit":
            print("👋 Goodbye!")
            break


if __name__ == "__main__":
    main()
