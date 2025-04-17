from experience import Experience
from education import Education
from headline import Headline

class Profile:
    def __init__(self):
        self.education: Education = []
        self.experience: Experience = []
        self._headline: Headline = None

    def add_education(self, university: str, from_year: str, to_year: str):
        education = Education(university, from_year, to_year)
        self.education.append(education)
    
    def add_experience(self, company: str, from_year: str, to_year: str):
        experience = Experience(company, from_year, to_year)
        self.experience.append(experience)
    
    def add_headline(self, headline_summary: str):
        headline = Headline(headline_summary)
        self._headline = headline
    
    
