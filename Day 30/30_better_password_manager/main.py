from characters import letters, numbers, symbols
import random
import pandas as pd
import tkinter as tk
import json
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
    pass_dict = {web: {"username":mail, "password":password}}
    if web != "" and mail != "" and password != "":
        try:
            with open("100_days_of_python\Day 30\\30_better_password_manager\log.json", mode="r") as file:
                data = json.load(file)
                data.update(pass_dict)
        except:
            with open("100_days_of_python\Day 30\\30_better_password_manager\log.json", mode="w") as file:
                json.dump(pass_dict, file, indent=4)
        else:
            with open("100_days_of_python\Day 30\\30_better_password_manager\log.json", mode="w") as file:
                json.dump(data, file, indent=4)
    else:
        error_window()

# ---------------------------- SEARCH ------------------------------- #
def search():
    try:
        with open("100_days_of_python\Day 30\\30_better_password_manager\log.json", mode="r") as file:
            web = input_website.get()
            data = json.load(file)
            mail = data[web]['username']
            password = data[web]['password']
    except:
        web = "Web not registered"
        mail = ""
        password = ""
    finally:
        info_window = tk.Tk()
        info_window.wm_title("Window")
        info_window.config(padx=20, pady=20)
        info_window.minsize(300, 300)
        title = tk.Label(info_window, text=f"{web}", font=("Arial", 24, "bold"))
        title.pack()
        user_label = tk.Label(info_window, text=f"Username: {mail}")
        user_label.pack()
        pw_label = tk.Label(info_window, text=f"Password: {password}")
        pw_label.pack()

# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
window.minsize(300, 300)

title_label = tk.Label(text="PASSWORD GENERATOR", font=("Arial", 24, "bold"))
title_label.grid(column=3, row=0, columnspan = 2)

canvas = tk.Canvas(height=300, width=300)
logo = tk.PhotoImage(file="100_days_of_python\Day 30\\30_better_password_manager\logo.png")
canvas.create_image(150, 150, image=logo)
canvas.grid(column=3, row=1, columnspan = 2)

label_website = tk.Label(text="Website:", font=("Arial", 16, "bold"))
label_website.grid(column=2, row=2)
input_website = tk.Entry(width=45)
input_website.grid(column=3, row=2, columnspan = 2, sticky='W')

button_search = tk.Button(window, text="Search", padx=50, command=search)
button_search.grid(column=4, row=2, columnspan = 2)

label_username = tk.Label(text="Username:", font=("Arial", 16, "bold"))
label_username.grid(column=2, row=3)
input_username = tk.Entry(width=80)
input_username.grid(column=3, row=3, columnspan = 2, sticky='W')

label_password = tk.Label(text="Password:", font=("Arial", 16, "bold"))
label_password.grid(column=2, row=4)
input_password = tk.Entry(window, width=45)
input_password.grid(column=3, row=4,)

button_generate = tk.Button(window, text="Generate Pass", padx=50, command=button_generate)
button_generate.grid(column=4, row=4, columnspan = 2)

button_add = tk.Button(text="Add", padx=220, command=save_generated)
button_add.grid(column=3, row=5, columnspan = 2)

window.mainloop()