from LogLevel import LogLevel
from LogConfig import LogConfig
from ConsoleAppender import ConsoleAppender
from LogMessage import LogMessage
from LoggingService import LogService
class Demo:
    def run():
        config = LogConfig(LogLevel.DEBUG, ConsoleAppender())
        log_service = LogService()
        log_service.set_config(config)

        log_service.debug("This is a debug message")

if __name__ == "__main__":
    Demo.run()
