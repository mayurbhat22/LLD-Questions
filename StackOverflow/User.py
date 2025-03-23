class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.questions = []
        self.answers = []
        self.comments = []

    def ask_question(self, question):
        self.questions.append(question)
    
    def answer_question(self, question, answer):
        self.answers.append((question, answer))
    
    def comment_on(self, commentable, comment):
        commentable.add_comments(comment)
        self.comments.append(comment)
        