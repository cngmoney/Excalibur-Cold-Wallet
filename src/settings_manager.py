import json
from pathlib import Path

SETTINGS_FILE = Path("data/settings.json")

DEFAULT_SETTINGS = {
    "theme": "dark",
    "language": "en",
    "currency_display": "RLUSD",
    "security": {
        "require_password": True,
        "require_nfc": True,
        "auto_lock_minutes": 5
    },
    "notifications": {
        "enable_sounds": True,
        "enable_led": False
    }
}

class SettingsManager:
    def __init__(self):
        self.settings = self.load_settings()

    def load_settings(self):
        if SETTINGS_FILE.exists():
            try:
                with open(SETTINGS_FILE, 'r') as f:
                    return json.load(f)
            except Exception:
                return DEFAULT_SETTINGS.copy()
        else:
            return DEFAULT_SETTINGS.copy()

    def save_settings(self):
        with open(SETTINGS_FILE, 'w') as f:
            json.dump(self.settings, f, indent=4)

    def get_setting(self, key_path):
        keys = key_path.split(".")
        ref = self.settings
        for key in keys:
            ref = ref.get(key, {})
        return ref

    def update_setting(self, key_path, value):
        keys = key_path.split(".")
        ref = self.settings
        for key in keys[:-1]:
            ref = ref.setdefault(key, {})
        ref[keys[-1]] = value
        self.save_settings()

# Example usage:
if __name__ == "__main__":
    sm = SettingsManager()
    print("Current Theme:", sm.get_setting("theme"))
    sm.update_setting("security.auto_lock_minutes", 10)
    print("Updated Lock Time:", sm.get_setting("security.auto_lock_minutes"))
