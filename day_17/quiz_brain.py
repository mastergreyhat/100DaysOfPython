class QuizBrain:
    def __init__(self, q_list):
        self.num = 0
        self.list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.num < len(self.list)

    def next_question(self):
        current_question = self.list[self.num]
        self.num += 1
        user_answer = input(f"Q.{self.num}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == str(correct_answer).lower():
            self.score += 1
            print("Correct!")
        else:
            print("Wrong!")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.num}\n")