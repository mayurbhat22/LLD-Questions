class User:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.posts = []
        self.answers = []
        self.comments = []
    
    def add_posts(self, post):
        self.posts.append(post)
    
    def add_answers(self, answer):
        self.answers.append(answer)
    
    def add_comments(self, comment):
        self.comments.append(comment)
