class Comment:
    def __init__(self, user, content):
        self.id = id(self)
        self.user = user
        self.content = content
    