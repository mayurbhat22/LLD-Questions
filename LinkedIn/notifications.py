from user import User
class Notifications:
    """
    A simple observer-based notification system.
    Observers (users) can register to be notified when certain events occur.
    """
    def __init__(self, type, notification_message, notification_date):
        self.type = type
        self.notification_message = notification_message
        self.notification_date = notification_date
        