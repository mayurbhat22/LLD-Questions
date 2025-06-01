from LogLevel import LogLevel
from LogConfig import LogConfig
from LogAppender import LogAppender
from LogMessage import LogMessage
class LogService:
    def __init__(self):
        self.config = None
    
    def set_config(self, config):
        self.config = config
    
    def log(self, log_level, message):
        if self.config and log_level.value >= self.config.get_log_level():
            log_message = LogMessage(log_level, message)
            self.config.get_log_appender().append(log_message.format())
    
    def debug(self, message):
        self.log(LogLevel.DEBUG, message)
    
    def info(self, message):
        self.log(LogLevel.INFO, message)
    
    def warning(self, message):
        self.log(LogLevel.WARNING, message)
    
    def error(self, message):
        self.log(LogLevel.ERROR, message)
    
    def fatal(self, message):
        self.log(LogLevel.FATAL, message)
