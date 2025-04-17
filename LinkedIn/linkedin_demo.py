from education import Education
from headline import Headline
from profile import Profile
from user import User
from connections import Connections
from datetime import datetime
from linkedin_system import LinkedInSystem
from notifications import Notifications
class LinkedInDemo:
    def run():
        linkedin_system = LinkedInSystem.get_instance()

        #Create users
        mayur = linkedin_system.create_user("Mayur", "may@gmail.com", "666555")
        kirtan = linkedin_system.create_user("Kirtan", "kir@gmail.com", "444555")

        #Add Education
        linkedin_system.user_add_education(mayur, "Indiana University", "2023", "2025")
        linkedin_system.user_add_education(kirtan, "Indiana University", "2023", "2025")

        #Add Experience
        linkedin_system.user_add_experience(mayur, "Microsoft", "2025", "2035")

        #Subscribe to Notification Service
        Notifications().add_observer(mayur)
        Notifications().add_observer(kirtan)
        #Send Request
        linkedin_system.send_connection_request(mayur, kirtan)


if __name__ == "__main__":
    demo = LinkedInDemo
    demo.run()



