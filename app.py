from tkinter import *
from PIL import Image, ImageTk
from googletrans import Translator

# Create a window
root = Tk()
root.title("Google Translate")
root.geometry("500x630")
root.iconbitmap("assets/logo.ico")

# Dispaly Google window
load = Image.open("assets/background.png")
render = ImageTk.PhotoImage(load)
img = Label(root, image=render)
img.place(x=0, y=0)
name = Label(root, text="Google Translate", fg="#FFFFFF", bd=0, bg="#03152D")
name.config(font=("Transformers Movie", 30))
name.pack(pady=10)

# Function to translate
def translate():
    INPUT = box_src.get(1.0, END)
    translator = Translator(service_urls=['translate.googleapis.com'])
    src_lang = translator.detect(INPUT)
    result = translator.translate(INPUT, src=src_lang.lang, dest="vi")
    box_dest.delete(1.0, END)
    box_dest.insert(END, result.text)
    

#Function to clear
def clear():
    box_src.delete(1.0, END)
    box_dest.delete(1.0, END)

# Create a text box
box_src = Text(root, width=28, height=8, font=("ROBOTO", 16))
box_src.pack(pady=20)

# Translate button
button_frame = Frame(root).pack(side=BOTTOM)


clear_button = Button(button_frame, text="Clear Text", font=("Arial", 10, 'bold'), fg="#FFFFFF", bg="#303030", command=clear)
clear_button.place(x=150, y=310)
trans_button = Button(button_frame, text="Translate", font=("Arial", 10, 'bold'), fg="#FFFFFF", bg="#303030", command=translate)
trans_button.place(x=290, y=310)

# Create a text box
box_dest = Text(root, width=28, height=8, font=("ROBOTO", 16))
box_dest.pack(pady=50)


root.mainloop()
