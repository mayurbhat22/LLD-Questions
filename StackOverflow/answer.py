from Commentable import Commentable

class Answer(Commentable):
    def __init__(self, question, content, user):
        self.question = question
        self.content = content
        self.user = user
        self.comments = []
    
    def add_comments(self, comment):
        self.comments.append(comment)

    