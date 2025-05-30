from Education import Education
from Experience import Experience

class Profile:
    def __init__(self):
        self.education = []
        self.experience = []
        self.headline = ""

    def add_education(self, university_name, degree, start_year, end_year):
        education = Education(university_name, degree, start_year, end_year)
        self.education.append(education)
    
    def add_experience(self, company_name, start_year, end_year):
        experience = Experience(company_name, start_year, end_year)
        self.experience.append(experience)
    