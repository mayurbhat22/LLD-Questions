from User import User
from Posts import Posts
from Answers import Answer
from Stackoverflow_service import QuestionService, AnswerService, CommentService

class Demo:
    def run():
        mayur = User(1, "Mayur", "mayur@xyz.com")
        kirtan = User(2, "Kirtan", "kirtan@xyz.com")
        shreyas = User(3, "Shreyas", "shreyas@xyz.com")

        post1 = QuestionService().create_post("Why is python slower than C++", "Can anyone explain wht python is slower", ["python", "C++"], mayur)
        answer1 = AnswerService().create_answer(post1, "C++ is interpret language", kirtan)
        comment1 = CommentService().add_comment(post1, shreyas, "A very good question!")
        comment2 = CommentService().add_comment(answer1, shreyas, "A detailed answer would be great")

        