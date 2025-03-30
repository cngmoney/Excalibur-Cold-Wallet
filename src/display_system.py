# display_system.py

import time
import os

class DisplaySystem:
    def __init__(self):
        self.logo_frames = [
            "[   ]", "[=  ]", "[== ]", "[===]", "[ ==]", "[  =]", "[   ]", "[  =]", "[ ==]", "[===]", "[== ]", "[=  ]"
        ]
        self.clear_command = "cls" if os.name == "nt" else "clear"

    def clear_screen(self):
        os.system(self.clear_command)

    def show_startup_animation(self):
        self.clear_screen()
        print("Initializing Excalibur Cold Wallet...\n")
        for i in range(2):  # Spin through the frames twice
            for frame in self.logo_frames:
                self.clear_screen()
                print(f"      {frame}")
                print("    Excalibur Protocol Coin Emblem\n")
                time.sleep(0.1)

        self.clear_screen()
        print("     [ * ] Excalibur Protocol Coin Emblem")
        print("   Powered by the Excalibur Protocol\n")
        time.sleep(1)

    def display_message(self, message):
        print(f"[DISPLAY]: {message}")

    def display_error(self, error_message):
        print(f"[ERROR]: {error_message}")

    def display_success(self, success_message):
        print(f"[SUCCESS]: {success_message}")
