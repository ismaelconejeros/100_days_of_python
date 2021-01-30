import tkinter as tk
import html

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20)
        self.window.configure(background=THEME_COLOR)
        self.window.minsize(350, 400)

        self.canvas = tk.Canvas(width=300, height=250)
        self.question = self.canvas.create_text(150, 125, text="", width=250, font=("Arial", 20, "italic"))
        self.canvas.grid( row=2, column=1, columnspan=3)

        self.label_score = tk.Label(text=f"Score: {self.score}", bg=THEME_COLOR, fg="white")
        self.label_score.grid(column=2, row=3)

        self.button_true = tk.PhotoImage(file='100_days_of_python\Day 34\\31_quizz_app\images\\true.png')
        self.b_true = tk.Button(image=self.button_true, command=self.button_true_func)
        self.b_true.grid(row=4, column=1)

        self.button_false = tk.PhotoImage(file='100_days_of_python\Day 34\\31_quizz_app\images\\false.png')
        self.b_false = tk.Button(image=self.button_false, command=self.button_false_func)
        self.b_false.grid(row=4, column=3)

        self.next_question()

        self.window.mainloop()

    def next_question(self):
        if self.question_number < len(self.question_list):
            self.current_question = self.question_list[self.question_number]
            self.question_number += 1
            q_text = html.unescape(self.current_question.text)
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.itemconfig(self.question, text=f"Final result\n{self.score} / {len(self.question_list)}")
            self.b_true.config(command="")
            self.b_false.config(command="")

    def button_true_func(self):
        correct_answer = self.current_question.answer
        if correct_answer == "True":
            self.score += 1
            self.label_score.config(text=f"Score: {self.score}")
        self.next_question()

    def button_false_func(self):
        correct_answer = self.current_question.answer
        if correct_answer == "False":
            self.score += 1
            self.label_score.config(text=f"Score: {self.score}")
        self.next_question()


        






    

