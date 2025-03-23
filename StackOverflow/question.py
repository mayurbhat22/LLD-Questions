from Commentable import Commentable

class Question(Commentable):
    def __init__(self, title, content, user):
        self.title = title
        self.answers = []
        self.content = content
        self.user = user
        self.comments = []
    
    def add_answer(self, answer):
        if answer not in self.answers:
            self.answers.append(answer)
    
    def add_comments(self, comment):
        self.comments.append(comment)