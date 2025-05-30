from User import User
from Profile import Profile
from Connections import Connection
from LinkedIn_Service import UserService, ConnectionService
class LinkedInDemo:
    def run():
        mayur = UserService().create_user("Mayur", "mayu@gmail.com", "8123333333")
        mayur.profile.add_education("Indiana", "Masters-Computer Science",2023,2025)
        mayur.profile.add_experience("Aurigo", 2021, 2023)

        kirtan = UserService().create_user("Kirtan", "kirtan@xyz.com", "1121121123")
        kirtan.profile.add_education("Indiana", "Masters-Computer Science",2023,2025)
        kirtan.profile.add_experience("ISRO", 2022, 2022)