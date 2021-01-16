from question_model import Question
from data import get_questions
from quiz_brain import QuizBrain


question_bank = []

question_data = get_questions()

for question in question_data:
    question = Question(question["question"], question["correct_answer"])
    question_bank.append(question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz.")
print(f"You final score is: {quiz.score}/{quiz.question_number}")