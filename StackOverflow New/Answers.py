from Comments import Comment
from Commentable import Commentable
from Question import Question
from User import User
class Answer(Commentable):
    def __init__(self, answer_id, question: Question, body, created_by: User):
        self.answer_id = answer_id
        self.post = question
        self.body = body
        self.created_by = created_by
        self.votes = 0
        self.comments = []
    
    def add_comments(self, comment: Comment):
        self.comments.append(comment)
    
    def add_vote(self, count):
        self.votes += count
    
