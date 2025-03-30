# button_interface.py

import RPi.GPIO as GPIO
import time

class ButtonInterface:
    def __init__(self, pin=17):
        self.button_pin = pin
        self.setup_button()

    def setup_button(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def wait_for_press(self, message="Press the button to continue..."):
        print(message)
        while GPIO.input(self.button_pin):
            time.sleep(0.1)
        print("Button pressed!")

    def is_pressed(self):
        return not GPIO.input(self.button_pin)

    def cleanup(self):
        GPIO.cleanup(self.button_pin)
