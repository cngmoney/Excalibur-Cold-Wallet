import time
from sensor_manager import SensorManager
from storage_handler import StorageHandler

class TamperDetection:
    def __init__(self):
        self.sensor_manager = SensorManager()
        self.storage_handler = StorageHandler()
        self.enabled = True

    def monitor(self):
        print("🔒 Tamper detection system active.")
        while self.enabled:
            sensors = self.sensor_manager.read_all()
            if sensors['tamper_switch']:
                self.handle_tamper()
            time.sleep(2)

    def handle_tamper(self):
        print("⚠️ Tamper event detected! Initiating security protocol...")
        self.wipe_sensitive_data()
        self.enabled = False  # Halt further monitoring

    def wipe_sensitive_data(self):
        secure_dir = self.storage_handler.STORAGE_DIR
        if not secure_dir.exists():
            print("No secure data found to wipe.")
            return

        for file in secure_dir.glob("*.enc"):
            try:
                file.unlink()
                print(f"🗑️ Wiped: {file.name}")
            except Exception as e:
                print(f"❌ Failed to delete {file.name}: {e}")

# Example usage:
if __name__ == "__main__":
    td = TamperDetection()
    td.monitor()
