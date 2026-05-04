from question_model import Question
from data import question_data
from quiz_brain import QuestionBrain

question_bank = []

for question in question_data:
    question_text = question['text']
    question_answer = question['answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuestionBrain(question_bank)

while quiz.stil_has_question():
    quiz.next_question()

print("You've completed quiz game!")
print(f"You're final score was {quiz.score}/{quiz.question_number}")