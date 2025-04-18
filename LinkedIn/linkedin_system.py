from education import Education
from headline import Headline
from profile import Profile
from user import User
from connections import Connections
from datetime import datetime
from notifications import Notifications
from jobpostings import JobPostings
from notifications import Notifications
from notifications_type import NotificationType
from collections import defaultdict
class LinkedInSystem:
    _instance = None

    def __init__(self):
        if LinkedInSystem._instance is not None:
            raise Exception("Only one instance can be created")
        LinkedInSystem._instance = self
        self.users = []
        self.job_postings = []
        self.notifications = defaultdict(list)
    
    @staticmethod
    def get_instance():
        if LinkedInSystem._instance is None:
            LinkedInSystem()
        return LinkedInSystem._instance

    def create_user(self, name, email, phone_number):
        user = User(name, email, phone_number)
        self.users.append(user)
        return user
    
    def post_job_posting(self, job: JobPostings):
        self.job_postings.append(job)
        for user in self.users:
            notification = Notifications(NotificationType.JOB_POSTING, "A job has been posted", datetime.now())
            self.add_notification(notification, user)
    
    def search_job_posting(self):
        for job in self.job_postings:
            print(f"Role: {job.title}")
            print(f"Posted Date: {job.posted_date}")
            print(f"Company: {job.company}")

    def add_notification(self, notification, user):
        self.notifications[user._email].append(notification)
    
    def get_notifications(self, user_email):
        return self.notifications[user_email]