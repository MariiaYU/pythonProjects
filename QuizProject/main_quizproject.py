from question_model_quizproject import Question
from data_quizproject import question_data

question_bank = []
for each_question in question_data:
    question_text = each_question["text"]
    question_answer = each_question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)





