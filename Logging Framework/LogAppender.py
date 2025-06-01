from abc import ABC, abstractmethod
class LogAppender:
    @abstractmethod
    def append(self, message):
        pass
