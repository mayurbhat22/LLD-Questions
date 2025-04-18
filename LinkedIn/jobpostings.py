class JobPostings:
    def __init__(self, title, description, posted_date, user, company=None):
        self.title = title
        self.description = description
        self.posted_date = posted_date
        self.user = user
        self.company = company
    