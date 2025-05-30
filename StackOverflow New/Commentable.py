from abc import ABC, abstractmethod
from Comments import Comment
class Commentable:
    @abstractmethod
    def add_comments(self, comment: Comment):
        pass