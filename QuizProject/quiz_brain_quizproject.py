class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ").lower()
        self.check_answer(user_answer, current_question.answer)

    def still_has_question(self):
        if self.question_number>=len(self.question_list):
            return False
        else:
            return True

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer.lower():
            self.score += 1
            print(f"Correct!")
        else:
            print(f"That is wrong answer.")
        print(f"The answer was: {correct_answer}.\nYour score is {self.score} / {self.question_number}\n")




