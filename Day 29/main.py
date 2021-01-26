from characters import letters, numbers, symbols
import random
import pandas as pd
import tkinter as tk
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    pass_letters = [random.choice(letters) for i in range(random.randint(4,6))]
    pass_numbers = [random.choice(numbers) for i in range(random.randint(4,6))]
    pass_symbols = [random.choice(symbols) for i in range(random.randint(4,6))]
    pass_list = pass_letters + pass_numbers + pass_symbols
    random.shuffle(pass_list)
    return "".join(pass_list)

def button_generate():
    input_password.delete(0, "end")
    input_password.insert(0, generate())

# ---------------------------- SAVE PASSWORD ------------------------------- #
def confirmation_window(a, b, c):
    def ok(a,b,c):
        data_dict = {"website": a, "username": b, "password": c}
        data = pd.DataFrame(data_dict, index=[0])
        data.to_csv('100_days_of_python\Day 29\log.csv', mode = 'a', sep="|", header=0)
    confirmation_window = tk.Tk()
    confirmation_window.wm_title("Window")
    confirmation_window.config(padx=20, pady=20)
    confirmation_window.minsize(300, 300)
    title = tk.Label(confirmation_window, text="Please Confirm:", font=("Arial", 24, "bold"))
    title.grid(row=0, column=0, columnspan = 2)
    website = tk.Label(confirmation_window, text=f"Website: ", font=("Arial", 16, "bold"))
    website.grid(row=1, column=0)
    website_ans = tk.Label(confirmation_window, text=f"{a}", font=("Arial", 16, "bold"))
    website_ans.grid(row=1, column=1)
    mail = tk.Label(confirmation_window, text=f"Username: ", font=("Arial", 16, "bold"))
    mail.grid(row=2, column=0)
    mail_ans = tk.Label(confirmation_window, text=f"{b}", font=("Arial", 16, "bold"))
    mail_ans.grid(row=2, column=1)
    password = tk.Label(confirmation_window, text=f"Password: ", font=("Arial", 16, "bold"))
    password.grid(row=3, column=0)
    password_ans = tk.Label(confirmation_window, text=f"{c}", font=("Arial", 16, "bold"))
    password_ans.grid(row=3, column=1)
    buttonok = tk.Button(confirmation_window, text=f"OK", padx=40, command=ok(a,b,c))
    buttonok.grid(row=4, column=0)

def error_window():
    confirmation_window = tk.Tk()
    confirmation_window.wm_title("Window")
    confirmation_window.config(padx=20, pady=20)
    confirmation_window.minsize(300, 300)
    title = tk.Label(confirmation_window, text="ERROR\nMISSING FIELDS", font=("Arial", 24, "bold"))
    title.grid(row=0, column=0, columnspan = 2)
    
def save_generated():
    web = input_website.get()
    mail = input_username.get()
    password = input_password.get()
    if web != "" and mail != "" and password != "":
        confirmation_window(web, mail, password)
    else:
        error_window()

# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
window.minsize(300, 300)

title_label = tk.Label(text="PASSWORD GENERATOR", font=("Arial", 24, "bold"))
title_label.grid(column=3, row=0, columnspan = 2)

canvas = tk.Canvas(height=300, width=300)
logo = tk.PhotoImage(file="100_days_of_python\Day 29\logo.png")
canvas.create_image(150, 150, image=logo)
canvas.grid(column=3, row=1, columnspan = 2)

label_website = tk.Label(text="Website:", font=("Arial", 16, "bold"))
label_website.grid(column=2, row=2)
input_website = tk.Entry(width=80)
input_website.grid(column=3, row=2, columnspan = 2)

label_username = tk.Label(text="Username:", font=("Arial", 16, "bold"))
label_username.grid(column=2, row=3)
input_username = tk.Entry(width=80)
input_username.grid(column=3, row=3, columnspan = 2)

label_password = tk.Label(text="Password:", font=("Arial", 16, "bold"))
label_password.grid(column=2, row=4)
input_password = tk.Entry(window, width=45)
input_password.grid(column=3, row=4,)

button_generate = tk.Button(window, text="Generate Pass", padx=50, command=button_generate)
button_generate.grid(column=4, row=4, columnspan = 2)

button_add = tk.Button(text="Add", padx=220, command=save_generated)
button_add.grid(column=3, row=5, columnspan = 2)

window.mainloop()