import time
import random

class SensorManager:
    def __init__(self):
        # Future: Initialize GPIO pins for tamper switch, motion sensor, temp sensor, etc.
        self.sensors = {
            "tamper_switch": False,  # False = not triggered
            "motion_sensor": False,
            "temperature_sensor": 25.0  # Default simulated temp (°C)
        }

    def read_tamper_switch(self):
        # Replace with GPIO input in production
        self.sensors["tamper_switch"] = random.choice([False, False, False, True])  # Simulate rare trigger
        return self.sensors["tamper_switch"]

    def read_motion_sensor(self):
        # Replace with GPIO input in production
        self.sensors["motion_sensor"] = random.choice([False, True])
        return self.sensors["motion_sensor"]

    def read_temperature_sensor(self):
        # Replace with I2C or analog sensor read
        self.sensors["temperature_sensor"] += random.uniform(-0.3, 0.3)
        return round(self.sensors["temperature_sensor"], 2)

    def read_all(self):
        return {
            "tamper_switch": self.read_tamper_switch(),
            "motion_sensor": self.read_motion_sensor(),
            "temperature_sensor": self.read_temperature_sensor()
        }

# Example usage:
if __name__ == "__main__":
    sm = SensorManager()
    while True:
        readings = sm.read_all()
        print("\nSensor Readings:", readings)
        if readings["tamper_switch"]:
            print("⚠️ Tamper switch triggered!")
        if readings["motion_sensor"]:
            print("👀 Motion detected!")
        time.sleep(2)
