from abc import ABC
class Notification(ABC):
    def send(self, messahe:str):
        pass

class SMSNotification(Notification):
    def send(self, message:str):
        print(f"SMS Notification: {message}")

class EmailNotification(Notification):
    def send(self, message:str):
        print(f"Email Notification: {message}")

class PushNotification(Notification):
    def send(self, message:str):
        print(f"Push Notification: {message}")

