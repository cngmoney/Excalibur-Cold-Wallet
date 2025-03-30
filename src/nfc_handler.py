import time
import nfc

class NFCHandler:
    def __init__(self):
        self.clf = None

    def connect(self):
        try:
            self.clf = nfc.ContactlessFrontend('usb')
            print("✅ NFC reader connected.")
        except Exception as e:
            print("❌ Failed to connect to NFC reader:", e)
            self.clf = None

    def read_uid(self, timeout=5):
        if not self.clf:
            print("NFC reader not initialized.")
            return None

        print("📡 Waiting for NFC tag...")
        tag = self.clf.connect(rdwr={'on-connect': lambda tag: False}, timeout=timeout)
        if tag:
            uid = tag.identifier.hex().upper()
            print(f"✅ Tag detected. UID: {uid}")
            return uid
        else:
            print("⏱️ No tag detected within timeout.")
            return None

    def close(self):
        if self.clf:
            self.clf.close()
            print("🔌 NFC reader disconnected.")
            self.clf = None

# Example usage:
if __name__ == "__main__":
    handler = NFCHandler()
    handler.connect()
    uid = handler.read_uid()
    handler.close()
