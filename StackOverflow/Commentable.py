from abc import ABC, abstractmethod
from comments import Comment
class Commentable:
    @abstractmethod
    def add_comments(self, comment: Comment):
        pass