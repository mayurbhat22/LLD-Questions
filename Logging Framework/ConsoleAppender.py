from LogAppender import LogAppender
class ConsoleAppender(LogAppender):
    def append(self, message):
        print(message)
        