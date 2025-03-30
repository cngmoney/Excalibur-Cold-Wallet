# error_logger.py

import datetime

class ErrorLogger:
    def __init__(self, log_file="error_log.txt"):
        self.log_file = log_file

    def log_error(self, error_message):
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        entry = f"[{timestamp}] ERROR: {error_message}\n"
        with open(self.log_file, 'a') as f:
            f.write(entry)
        print(entry.strip())  # Also print to terminal
