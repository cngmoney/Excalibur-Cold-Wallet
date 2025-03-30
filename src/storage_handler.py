import os
import json
from pathlib import Path
from cryptography.fernet import Fernet

STORAGE_DIR = Path("data/secure")
KEY_FILE = Path("data/master.key")

class StorageHandler:
    def __init__(self):
        STORAGE_DIR.mkdir(parents=True, exist_ok=True)
        self.key = self.load_or_generate_key()
        self.cipher = Fernet(self.key)

    def load_or_generate_key(self):
        if not KEY_FILE.exists():
            key = Fernet.generate_key()
            with open(KEY_FILE, 'wb') as f:
                f.write(key)
            return key
        with open(KEY_FILE, 'rb') as f:
            return f.read()

    def encrypt_and_store(self, filename, data):
        filepath = STORAGE_DIR / filename
        json_data = json.dumps(data).encode()
        encrypted = self.cipher.encrypt(json_data)
        with open(filepath, 'wb') as f:
            f.write(encrypted)
        print(f"✅ Data securely saved to {filepath}")

    def load_and_decrypt(self, filename):
        filepath = STORAGE_DIR / filename
        if not filepath.exists():
            print(f"❌ File {filepath} does not exist.")
            return None
        with open(filepath, 'rb') as f:
            encrypted = f.read()
        try:
            decrypted = self.cipher.decrypt(encrypted)
            return json.loads(decrypted.decode())
        except Exception as e:
            print("❌ Failed to decrypt data:", e)
            return None

# Example usage:
if __name__ == "__main__":
    sh = StorageHandler()
    test_data = {"wallet": "0xABC123", "balance": 1000.0}
    sh.encrypt_and_store("wallet_data.enc", test_data)
    loaded = sh.load_and_decrypt("wallet_data.enc")
    print("🔓 Decrypted Data:", loaded)
