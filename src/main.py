# main.py
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

from auth_system import AuthSystem
from button_interface import ButtonInterface
from crypto_processor import CryptoProcessor
from display_system import DisplaySystem
from nfc_handler import NFCHandler
from sensor_manager import SensorManager
from tamper_detection import TamperDetection
from universal_handler import UniversalHandler
from user_input import UserInput
from ledger_system import LedgerSystem
from wallet_api import WalletAPI
from exchange_manager import ExchangeManager
from invoice_system import InvoiceSystem
from fiat_conversion import FiatConversion
from error_logger import ErrorLogger
from encryption_manager import EncryptionManager
from nfc_authenticator import NFCAuthenticator
from settings_manager import SettingsManager
from storage_handler import StorageHandler
from transaction_manager import TransactionManager
from blockchain_connector import BlockchainConnector

class ExcaliburColdWallet:
    def __init__(self):
        self.auth_system = AuthSystem()
        self.button_interface = ButtonInterface()
        self.crypto_processor = CryptoProcessor()
        self.display_system = DisplaySystem()
        self.nfc_handler = NFCHandler()
        self.sensor_manager = SensorManager()
        self.tamper_detection = TamperDetection()
        self.universal_handler = UniversalHandler()
        self.user_input = UserInput()
        self.ledger_system = LedgerSystem()
        self.wallet_api = WalletAPI()
        self.exchange_manager = ExchangeManager()
        self.invoice_system = InvoiceSystem()
        self.fiat_conversion = FiatConversion()
        self.error_logger = ErrorLogger()
        self.encryption_manager = EncryptionManager()
        self.nfc_authenticator = NFCAuthenticator()
        self.settings_manager = SettingsManager()
        self.storage_handler = StorageHandler()
        self.transaction_manager = TransactionManager()
        self.blockchain_connector = BlockchainConnector()
        
    def run(self):
        try:
            print("Starting Excalibur Cold Wallet...")
            self.display_system.show_startup_animation()
            
            if not self.auth_system.authenticate_user():
                print("Authentication Failed. Exiting...")
                return
            
            print("Authentication Successful.")
            self.universal_handler.initialize()
            
            while True:
                self.universal_handler.run()
                
        except KeyboardInterrupt:
            print("System Interrupted by User.")
        finally:
            self.cleanup()

    def cleanup(self):
        self.universal_handler.cleanup()
        print("System Cleanup Complete.")

if __name__ == "__main__":
    wallet = ExcaliburColdWallet()
    wallet.run()
