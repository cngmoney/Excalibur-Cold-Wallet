import time

class NFCAuthenticator:
    def __init__(self, authorized_uids=None):
        # Hardcoded or loaded list of authorized NFC tag UIDs
        self.authorized_uids = authorized_uids if authorized_uids else [
            "04A2243B5C6180",  # Example UID
        ]

    def read_nfc_tag(self):
        """
        Placeholder for NFC hardware integration.
        In production, connect to an NFC reader and return the UID of the scanned tag.
        """
        print("\n[Simulating NFC Tag Scan]")
        scanned_uid = input("Enter scanned NFC UID: ")
        return scanned_uid.strip().upper()

    def authenticate(self):
        scanned_uid = self.read_nfc_tag()
        if scanned_uid in self.authorized_uids:
            print("✅ NFC Authentication Successful.")
            return True
        else:
            print("❌ NFC Authentication Failed.")
            return False

    def add_authorized_uid(self, uid):
        uid = uid.strip().upper()
        if uid not in self.authorized_uids:
            self.authorized_uids.append(uid)
            print(f"✅ UID {uid} added to authorized list.")

# Example usage:
if __name__ == "__main__":
    nfc_auth = NFCAuthenticator()
    if nfc_auth.authenticate():
        print("Access Granted.")
    else:
        print("Access Denied.")
