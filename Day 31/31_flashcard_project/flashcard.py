import tkinter as tk
import random
import json
import pandas as pd

#------Preparing the data
def words(n):
    global est_dict
    data = pd.read_csv("100_days_of_python\Day 31\\31_flashcard_project\estonian_english.csv", header=0)
    df = pd.DataFrame(data)
    df2 = df.to_dict()
    est_dict = {df2['estonian'][i]:df2['english'][i] for i in range(n)}
    return est_dict

#----- Picking_word
def new_word():
    def english_word():
        canvas.itemconfig(flag, image=english_canvas)
        canvas.itemconfig(word_text, text=est_dict[est_word])
    canvas.itemconfig(flag, image=estonian_canvas)
    est_word = random.choice(words)
    canvas.itemconfig(word_text, text=est_word)
    print(est_word)
    print(est_dict[est_word])
    window.after(5000, english_word)
    return est_word

#------buttons
def start():
    fail_button.config(text="FAILED", command=fail)
    ok_button.config(text="GOT IT", command=gotit)
    new_word()

def fail():
    new_word()

def gotit():
    global score
    score += 1
    canvas.itemconfig(score_points, text=f"Score : {score}")
    new_word()

est_dict = words(100)
words = [i for i in est_dict]
score = 0
time_timer = 5

window = tk.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
window.minsize(900, 700)

canvas = tk.Canvas(width=900, height=700)
estonian_canvas = tk.PhotoImage(file="100_days_of_python\Day 31\\31_flashcard_project\\bg_est.png")
english_canvas = tk.PhotoImage(file="100_days_of_python\Day 31\\31_flashcard_project\\bg_en.png")
flag = canvas.create_image(450, 300, image=estonian_canvas)

score_points = canvas.create_text(450, 150, text=f"Score : {score}", font=("Ariel", 18, "italic"))
word_text = canvas.create_text(450, 500, text="Guess the Estonian Word", font=("Ariel", 40, "bold"))

canvas.config(bg='lightgreen')
canvas.grid(row=0, column=0, columnspan=10, rowspan=10)

timer_label = tk.Label(text="Press any button to begin", font=("Times New Roman", 18, "normal"), pady=50)
timer_label.grid(column=5, row=10)

fail_pic = tk.PhotoImage(file = "100_days_of_python\Day 31\\31_flashcard_project\\fail_button.png") 
fail_button = tk.Button(text="START", image=fail_pic, padx=30, pady=30, command=start)
fail_button.grid(column=3, row=10)
ok_pic = tk.PhotoImage(file = "100_days_of_python\Day 31\\31_flashcard_project\ok_button.png") 
ok_button = tk.Button(text="START", image=ok_pic, padx=30, pady=30, command=start)
ok_button.grid(column=7, row=10)

window.mainloop()