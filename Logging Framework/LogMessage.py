from datetime import datetime

class LogMessage:
    def __init__(self, log_level, message):
        self.time_stamp = datetime.now()
        self.level = log_level
        self.message = message
    
    def format(self):
        return f"[{self.time_stamp}] [{self.level}] {self.message}"
    