from Posts import Posts
from Question import Question
from Answers import Answer
from User import User
from Comments import Comment
class QuestionService:
    questions_count = 0

    def create_post(self, title, description, tags, created_by: User):
        QuestionService.questions_count += 1
        question = Question(QuestionService.questions_count, title, description, tags, created_by)
        created_by.add_posts(question)
        return question

class AnswerService:
    answer_count = 0

    def create_answer(self, question : Question, body, created_by: User):
        AnswerService.answer_count += 1
        answer = Answer(AnswerService.answer_count, question, body, created_by)
        question.add_answers(answer)
        created_by.add_answers(answer)
        return answer

class CommentService:
    comment_count = 0

    def add_comment(self, post, added_by: User, text):
        comment = Comment(CommentService.comment_count, text, added_by)
        post.add_comments(comment)
        added_by.add_comments(comment)
        return comment

