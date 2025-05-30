from Comments import Comment
from User import User
class Posts:
    def __init__(self, content, created_by: User):
        self.content = content
        self.created_by = created_by
        self.comments = []
        
    def add_comments(self, comment: Comment):
        self.comments.append(comment)

