from profile import Profile
from connections import Connections
from datetime import datetime

class User:
    def __init__(self, name, email, phone_number):
        self._name = name
        self._email = email
        self._phone_number = phone_number
        self.profile = Profile()
        self.connections: User = []
        self.pending_connections: Connections = []
    
    def add_education(self, university: str, from_year: str, to_year: str):
        self.profile.add_education(university, from_year, to_year)
        print("Education added")
    
    def add_experience(self, company: str, from_year: str, to_year: str):
        self.profile.add_experience(company, from_year, to_year)
        print("Experience added")
    
    def add_headline(self, headline_summary: str):
        self.profile.add_headline(headline_summary)
        print("Headline added")
    
    def send_connection_request(self, to_user):
        connection = Connections(self, to_user, datetime.now())
        to_user.pending_connections.append(connection)
        print(f"Connection request to {to_user._name} sent")
        return connection

    def accept_connection_request(self, from_user):
        for connection in self.pending_connections:
            if connection.from_user._email == from_user._email:
                self.connections.append(from_user)
                from_user.connections.append(self)
                self.pending_connections.remove(connection)
                print(f"{self._name} accepted {from_user._name}'s connection request!")
                break
    
    def recieve_connection_request(self, from_user):
        print(f"{from_user._name} sent a Connection request")

