import tkinter as tk

window = tk.Tk()
window.title("Mile to KM converter")
window.minsize(300,300)

def mile_to_km():
    miles = float(input_box.get())
    kms = miles * 1.6
    label_input.config(text=f"{miles} MILES")
    label_result.config(text=f"{kms} KMS")

def km_to_mile():
    kms = float(input_box.get())
    miles = kms / 1.6
    label_input.config(text=f"{kms} KMS")
    label_result.config(text=f"{miles:.2f} MILES")

def change_mode():
    button_convert.config(command=km_to_mile)
    label_input.config(text="KMS")
    label_result.config(text="MILES")

label_title = tk.Label(text="UNIT CONVERTER", font=("Arial", 24, "bold"))
label_title.grid(column=1, row=1)

button_mode = tk.Button(text="Change Mode", command=change_mode)
button_mode.grid(column=1, row=2)

label_input = tk.Label(text="MILES", font=("Arial", 18, "bold"))
label_input.grid(column=0, row=3)

label_equal = tk.Label(text="is equal to")
label_equal.grid(column=1, row=3)

label_result = tk.Label(text="KMs", font=("Arial", 18, "bold"))
label_result.grid(column=2, row=3)

input_box = tk.Entry()
input_box.grid(column=1, row=4)

button_convert = tk.Button(text="Convert", command=mile_to_km)
button_convert.grid(column=1, row=5)


window.mainloop()
