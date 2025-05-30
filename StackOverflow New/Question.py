from Comments import Comment
from User import User
from Commentable import Commentable
class Question(Commentable):
    def __init__(self, question_id, title, description, tags, created_by: User):
        self.question_id = question_id
        self.title = title
        self.description = description
        self.tags = tags
        self.created_by = created_by
        self.answers = []
        self.comments = []
    
    def add_answers(self, answer):
        self.answers.append(answer)
    
    def add_comments(self, comment: Comment):
        self.comments.append(comment)

