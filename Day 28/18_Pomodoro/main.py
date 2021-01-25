import tkinter as tk

colorbg = '#ffeebb'
mins =  24
secs = 60
counter = 1

def worktime():
    global mins, secs, counter
    stage_label['text'] = f'WORK TIME  ({counter}/7)'
    secs -= 1
    if counter <= 7:
        if secs > 9:
            minsecs['text']= f"{mins}:{secs}"
        elif secs > 0:
            minsecs['text']= f"{mins}:0{secs}"
        elif secs == 0:
            minsecs['text']= f"{mins}:0{secs}"
            secs = 60
            if mins != 0:
                mins -= 1
            else:
                counter += 1
                if counter%2 == 0:
                    stage_label['text'] = f'REST TIME  ({counter}/7)'
                    mins = 4
                else:
                    mins = 24
    else:
        mins = 29
    window.after(1000, worktime)

def reset():
    global mins, secs, counter
    stage_label['text'] = f'Pomodoro Clock'
    minsecs['text'] = "25:00"
    mins =  24
    secs = 60
    counter = 1


window = tk.Tk()
window.title("Pomodoro APP")
window.minsize(400, 300)
window.configure(background=colorbg)

img_tomato = tk.PhotoImage(file="100_days_of_python\Day 28\\18_Pomodoro\\tomato.png")
tomato = tk.Label(window, image = img_tomato, background=colorbg)
tomato.grid(column=1, row=1)

stage_label = tk.Label(text="Pomodoro Clock", font=("Arial", 34, "bold"), background=colorbg)
stage_label.grid(column=1, row=0)

minsecs = tk.Label(text="25:00", font=("Arial", 24, "bold"), background='#F26849')
minsecs.grid(column=1, row=1)

start = tk.Button(window, text = "Start", command=worktime, fg='white', bg='green', activebackground='red')
reset = tk.Button(window, text = "Reset", command= reset, fg='white', bg='green', activebackground='red')
start.grid(column=0, row=4)
reset.grid(column=2, row=4)

window.mainloop()
