from LogAppender import LogAppender
class FileAppender(LogAppender):
    def __init__(self, file):
        self.file = file

    def append(self, message):
        with open(self.file, 'a') as f:
            f.write(message + '\n')
            
        