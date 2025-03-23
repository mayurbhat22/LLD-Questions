from stackoverflow import StackOverFlow
from question import Question
from User import User
from answer import Answer

class StackOverFlowDemo:
    def run():
        stackoverflow = StackOverFlow()
        print("hello")
        john = stackoverflow.create_user("John", "abc@gmail.com")
        mayur = stackoverflow.create_user("Mayur", "xyz@gmail.com")
        kirtan = stackoverflow.create_user("Kirtan", "aaa@gmail.com")

        question_1 = stackoverflow.ask_question(john, "What is Python", "How is Python different from Java")
        answer_1 = stackoverflow.answer_question(mayur, question_1, "Python is easy to write, Java has lots of syntaxes")

        stackoverflow.add_comment(kirtan, question_1, "Great Question")
        stackoverflow.add_comment(kirtan, answer_1, "Answer could have been better")
        

        for user in stackoverflow.users:
            print(user.name)
            print(user.questions)
            print(user.answers)
            print(" ")
        

if __name__ == "__main__":
    StackOverFlowDemo.run()