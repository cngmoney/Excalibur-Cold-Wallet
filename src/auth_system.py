# auth_system.py
import getpass
import hashlib

class AuthSystem:
    def __init__(self):
        self.stored_hash = self.load_password_hash()

    def load_password_hash(self):
        try:
            with open("auth_hash.txt", "r") as f:
                return f.read().strip()
        except FileNotFoundError:
            return self.setup_new_password()

    def setup_new_password(self):
        print("🔐 First-time setup: Please create a new password.")
        password = getpass.getpass("Enter new password: ")
        confirm = getpass.getpass("Confirm new password: ")

        if password != confirm:
            print("❌ Passwords do not match. Try again.")
            return self.setup_new_password()

        hash_ = self.hash_password(password)
        with open("auth_hash.txt", "w") as f:
            f.write(hash_)
        print("✅ Password successfully created.")
        return hash_

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def authenticate_user(self):
        print("🔐 Please enter your password to continue.")
        attempts = 3
        while attempts > 0:
            password = getpass.getpass("Password: ")
            if self.hash_password(password) == self.stored_hash:
                return True
            else:
                attempts -= 1
                print(f"❌ Incorrect password. {attempts} attempts remaining.")
        return False
