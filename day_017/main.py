from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_bank.append(Question(text = question['text'], answer = question['answer']))

quizBrain = QuizBrain(question_bank)

while quizBrain.still_has_question():
    quizBrain.next_question()

quizBrain.report()