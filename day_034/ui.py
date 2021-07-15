THEME_COLOR = "#375362"
RED = "#ff0000"
GREEN = "#00ff00"
WHITE = "#fff"

from tkinter import * 
from quiz_brain import QuizBrain

class QuizInterface:

    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz

        self.window = Tk()
        self.window.title('Quiz')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.l_score = Label(text='Score: 0', bg=THEME_COLOR, fg='#fff', font=10)
        self.l_score.grid(row=0, column=1)

        self.canvas = Canvas(height=250, width=300)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280, 
            font="Arial 15 italic", 
            text="Click the bubbles that are multiples of two."
            )        
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)

        true_img = PhotoImage(file='images/true.png')
        self.b_true = Button(image=true_img, highlightthickness=0, command=self.go_true)
        self.b_true.grid(row=2, column=0)

        false_img = PhotoImage(file='images/false.png')
        self.b_false = Button(image=false_img, highlightthickness=0, command=self.go_false)
        self.b_false.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.configure(bg=WHITE)
        if self.quiz.still_has_questions():
            self.l_score.config(text=f'Score: {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text='End')
            self.b_false.config(state='disabled')
            self.b_true.config(state='disabled')

    def go_true(self):
        is_rigth = self.quiz.check_answer('true')
        self.give_fidback(is_rigth)

    def go_false(self):
        is_rigth = self.quiz.check_answer('false')
        self.give_fidback(is_rigth)

    def give_fidback(self, is_rigth):
        if is_rigth:
            self.canvas.configure(bg=GREEN)
        else:
            self.canvas.configure(bg=RED)
        self.window.after(1000, self.get_next_question)