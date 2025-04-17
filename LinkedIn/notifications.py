from user import User
class Notifications:
    """
    A simple observer-based notification system.
    Observers (users) can register to be notified when certain events occur.
    """
    def __init__(self):
        self.observers: list[User] = []

    def add_observer(self, user: User):
        if user not in self.observers:
            self.observers.append(user)
        print(self.observers)

    def notify_user(self, from_user: User, to_user: User):
        for user in self.observers:
            if user._email == to_user._email:
                user.recieve_connection_request(from_user)
                break
        