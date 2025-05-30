from Profile import Profile
from Connections import Connection
class User:
    def __init__(self, name, email, phone_number):
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.profile = Profile()
        self.connections = []
        self.pending_requests = []
    
    def add_connections(self, to_user):
        self.connections.append(to_user)
    
    def add_pending_request(self, connection: Connection):
        self.pending_requests.append(connection)