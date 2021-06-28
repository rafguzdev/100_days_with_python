class QuizBrain:

    def __init__(self, q_list):
        self.q_number = 0
        self.score = 0
        self.q_list = q_list
        
    def next_question(self):
        question = self.q_list[self.q_number]
        correct_answer = question.answer
        self.q_number += 1
        answer = input(f"Q.{self.q_number} {question.text} (True/False)?: ")
        self.check_answer(answer, correct_answer)

    def still_has_question(self):
        return self.q_number < len(self.q_list)

    def check_answer(self, answer, correct_answer):
        if answer.lower() == correct_answer.lower():
            self.score += 1
            print('OK')
        else:
            print('Fail')
        print(f'Current score: {self.score}/{self.q_number}')
        print('\n')

    def report(self):
        print('Quiz completed')
        print(f'Tour final score was: {self.score}/{self.q_number}')