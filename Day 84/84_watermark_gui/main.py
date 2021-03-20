from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image, ImageDraw, ImageFont

def add_img():
    global img, tk_img
    file_img = filedialog.askopenfilename(title="Image to add watermark")
    img = Image.open(file_img)
    if img.mode in ("RGBA", "P"):
        img = img.convert("RGB")
    tk_img = ImageTk.PhotoImage(img)
    panel.config(image=tk_img)
    panel.image = tk_img

def add_watermark():
    global width, height, img
    draw = ImageDraw.Draw(img)

    text = entry_watermark.get()
    font = ImageFont.load_default()
    textwidth, textheight = draw.textsize(text)

    width, height = img.size
    margin = 10
    x = width - textwidth - margin
    y = height - textheight - margin

    colors = img.getpixel((textwidth,textheight))
    print(colors)

    draw.text((x, y), text=text, font=font)
    img.save("100_days_of_python\Day 84\84_watermark_gui\\result.jpg")
    img = ImageTk.PhotoImage(Image.open("100_days_of_python\Day 84\84_watermark_gui\\result.jpg"))
    panel.config(image=img)
    panel.image = img

window = Tk()
window.title("Watermark App")
window.config(padx=40, pady=40, bg="yellow")

button_add_img = Button(text="Picture to watermark",bg="lightblue",command=add_img,padx=5,pady=25,font=("Arial", 18, "bold"))
button_add_img.grid(row=0, column=0)

button_watermark = Button(text="Add watermark", bg="lightblue", command=add_watermark, padx=35, pady=25, font=("Arial", 18, "bold"))
button_watermark.grid(row=1, column=0)

label_watermark = Label(text="Watermark", font=("Arial", 18, "bold"), bg="yellow")
label_watermark.grid(row=2, column=0)
entry_watermark = Entry(width=30)
entry_watermark.grid(row=3, column=0)

img = Image.open("100_days_of_python\Day 84\84_watermark_gui\example_forest.jpg")
img = img.resize((1000, 600))
width, height = img.size
tk_img = ImageTk.PhotoImage(img)
panel = Label(image=tk_img)
panel.image = tk_img
panel.grid(row=0, column=1, rowspan=4, padx=25)

window.mainloop()