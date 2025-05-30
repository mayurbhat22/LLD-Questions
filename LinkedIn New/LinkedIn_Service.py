from User import User
from Profile import Profile
from Connections import Connection
class UserService:
    def __init__(self):
        self.users = []

    def create_user(self, name, email, phone_number):
        user = User(name, email, phone_number)
        self.users.append(user)
        return user
    
class ConnectionService:
    def send_connection_request(self, from_user, to_user):
        if to_user in from_user.connections:
            return
        for conn in to_user.pending_connections:
            if conn.from_user.email == from_user.email:
                return
        connection = Connection(from_user, to_user)
        to_user.add_pending_request(connection)

    def accept_connection_request(self, receiver, sender):
        for conn in receiver.pending_connections:
            if conn.from_user.email == sender.email:
                receiver.pending_connections.remove(conn)
                receiver.add_connections(sender)
                sender.add_connections(receiver)
                break

    
    
