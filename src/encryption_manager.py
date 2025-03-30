# encryption_manager.py

from cryptography.fernet import Fernet

class EncryptionManager:
    def __init__(self, key=None):
        self.key = key or Fernet.generate_key()
        self.cipher = Fernet(self.key)

    def encrypt(self, plaintext):
        if isinstance(plaintext, str):
            plaintext = plaintext.encode()
        encrypted = self.cipher.encrypt(plaintext)
        return encrypted

    def decrypt(self, encrypted_data):
        try:
            decrypted = self.cipher.decrypt(encrypted_data).decode()
            return decrypted
        except Exception as e:
            print(f"[ERROR] Decryption failed: {e}")
            return None

    def get_key(self):
        return self.key
