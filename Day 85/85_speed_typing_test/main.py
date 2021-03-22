from timeit import default_timer
import tkinter as tk
import random
from nltk.corpus import words

word_list = words.words()

class TypingGame:
    def __init__(self):
        self.word = random.choice(word_list)
        self.score = 0
        self.create_window()

    def create_window(self):
        self.label_typing = tk.Label(text="TYPING TEST GAME", font=("Arial",20,"bold"))
        self.label_typing.pack()
        self.label_sentence = tk.Label(text=self.word,font=("Arial",20,"bold"))
        self.label_sentence.pack()
        self.entry = tk.Entry(width=50)
        self.entry.focus()
        self.entry.pack()
        self.button_done = tk.Button(text="DONE",font=("Arial",20,"bold"),command=self.new_word)
        self.button_done.pack()
        self.label_score = tk.Label(text=f"Score: {self.score}",font=("Arial",20,"bold"))
        self.label_score.pack()
        self.label_time = tk.Label(text=f"time: {default_timer()}",font=("Arial",20,"bold"))
        self.label_time.pack()

    def new_word(self, event=None):
        self.check()
        self.word = random.choice(word_list)
        self.label_sentence.config(text=self.word)
        self.label_score.config(text=f"Score: {self.score}")
        self.label_time.config(text=f"time: {default_timer()}")
        self.entry.delete(0,"end")

    def check(self):
        typed = self.entry.get()
        if self.word.lower() == typed.lower():
            self.score += 1
        

window = tk.Tk()
window.title("Typing Speed Test")
window.config(padx=50,pady=50)

game = TypingGame()
window.bind('<Return>', game.new_word)

window.mainloop()