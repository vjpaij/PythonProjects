from quiz_oop.question_model import Question
from quiz_oop.data import question_data
from quiz_oop.data_api import question_api
from quiz_oop.quiz_brain import QuizBrain
from quiz_oop.ui import QuizInterface

question_bank = []

for question in question_api:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface()

#below while statement is commented out when we use UI Interface as mainloop() acts like a while loop
# while quiz.still_has_questions():
#     quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
