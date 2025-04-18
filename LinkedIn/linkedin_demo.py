from education import Education
from headline import Headline
from profile import Profile
from user import User
from connections import Connections
from datetime import datetime
from linkedin_system import LinkedInSystem
from notifications import Notifications
from jobpostings import JobPostings
class LinkedInDemo:
    def run():
        linkedin_system = LinkedInSystem.get_instance()

        #Create users
        mayur = linkedin_system.create_user("Mayur", "may@gmail.com", "666555")
        kirtan = linkedin_system.create_user("Kirtan", "kir@gmail.com", "444555")

        #Add Education
        mayur.add_education("Indiana University", "2023", "2025")
        kirtan.add_education("Indiana University", "2023", "2025")

        #Add Experience
        mayur.add_experience("Microsoft", "2025", "2035")

        #Send Request
        mayur.send_connection_request(kirtan)

        #Accept Request
        kirtan.accept_connection_request(mayur)

        #Job Posting
        job = JobPostings("Software Engineer", "SDE-1", datetime.now(), mayur, "Microsoft")
        linkedin_system.post_job_posting(job)

        #Search Job Posting
        linkedin_system.search_job_posting()

        notifications = linkedin_system.get_notifications(mayur._email)
        for n in notifications:
            print(f"Notification Type: {n.type}")
            print(f"Message: {n.notification_message}")
            print(f"Date-Time: {n.notification_date}")

if __name__ == "__main__":
    demo = LinkedInDemo
    demo.run()



