from education import Education
from headline import Headline
from profile import Profile
from user import User
from connections import Connections
from datetime import datetime
from notifications import Notifications
class LinkedInSystem:
    _instance = None

    def __init__(self):
        if LinkedInSystem._instance is not None:
            raise Exception("Only one instance can be created")
        LinkedInSystem._instance = self
        self.users = []
    
    @staticmethod
    def get_instance():
        if LinkedInSystem._instance is None:
            LinkedInSystem()
        return LinkedInSystem._instance

    def create_user(self, name, email, phone_number):
        user = User(name, email, phone_number)
        self.users.append(user)
        return user
    
    def user_add_education(self, user: User, university: str, from_year: str, to_year: str):
        user.add_education(university, from_year, to_year)
    
    def user_add_experience(self, user: User, company: str, from_year: str, to_year: str):
        user.add_experience(company, from_year, to_year)
    
    def user_add_headline(self, user: User, headline_summary: str):
        user.add_headline(headline_summary)
    
    def send_connection_request(self, from_user: User, to_user: User):
        connection = from_user.send_connection_request(to_user)
        to_user.pending_connections.append(connection)
        Notifications().notify_user(from_user, to_user)

    