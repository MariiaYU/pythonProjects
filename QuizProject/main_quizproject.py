from question_model_quizproject import Question
from data_quizproject import question_data
from quiz_brain_quizproject import QuizBrain

question_bank = []
for each_question in question_data:
    question_text = each_question["question"]
    question_answer = each_question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_question():
    quiz_brain.next_question()

print(f"You've completed the Quiz!\n"f"Your final score is: {quiz_brain.score} / {len(question_bank)}")







