import tkinter as tk

window = tk.Tk()
window.title("My first GUI program")
window.minsize(700, 400)

#Label
my_label = tk.Label(text="This is a Label", font=("Arial", 24, "bold"))
#my_label.pack() #side, expand
##Ways to change the label atributes
my_label["text"] = "New Text"
my_label.config(text="New Label")
#my_label.place(x=0,y=0)
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)


#Buttons
def button_clicked():
    print("I got clicked")

button = tk.Button(text="This is a button", command=button_clicked)
#button.pack()
button.grid(column=1, row=1)

button2 = tk.Button(text="New Button")
button2.grid(column=3, row=0)

#Entry
input = tk.Entry()
#input.pack()
input.grid(column=4, row=2)





# #CHALLENGE: Make a button that change the label
# n = 0
# my_label = tk.Label(text=f"Label change N°:{n}", font=("Arial", 24, "bold"))
# my_label.pack()

# def button_clicked():
#     global n
#     n += 1
#     my_label["text"] = f"Label change N°:{n}"
    
# button = tk.Button(text="Change", command=button_clicked)
# button.pack()
#---------------------------

# #CHALLENGE: Make the label to print the entry
# my_label = tk.Label(text="This is a Label", font=("Arial", 24, "bold"))
# my_label.pack()

# input = tk.Entry()
# input.pack()

# def button_clicked():
#     new_text = input.get()
#     my_label["text"] = f"{new_text}"

# button = tk.Button(text="Change label", command=button_clicked)
# button.pack()
#------------------------------







window.mainloop()