from User import User
from question import Question
from answer import Answer
from comments import Comment
class StackOverFlow:
    def __init__(self):
        self.users = []
        self.questions = []
        self.answers = []
        self.comments = []
    
    def create_user(self, name, email):
        user = User(name, email)
        self.users.append(user)
        return user

    def ask_question(self, user, title, content):
        question = Question(title, content, user)
        user.ask_question(question)
        self.questions.append(question)
        return question
    
    def answer_question(self, user, question, content):
        answer = Answer(question, content, user)
        question.add_answer(answer)
        user.answer_question(question, answer)
        self.answers.append(answer)
        return answer

    def add_comment(self, user, commentable, comment):
        comments = Comment(user, comment)
        user.comment_on(commentable, comments)
        self.comments.append(comments)