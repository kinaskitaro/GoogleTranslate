from tkinter import *
from PIL import Image, ImageTk
from googletrans import Translator

# Create a window
root = Tk()
root.title("Google Translate")
root.geometry("500x660")
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
    lang_combo_value = lang_combo.get()
    if lang_combo_value == "Vietnamese":
        dest="vi"
    elif lang_combo_value == "Japanese":
        dest="ja"
    elif lang_combo_value == "Chinese":
        dest="zh-cn"
    elif lang_combo_value == "Korean":
        dest="ko"
    elif lang_combo_value == "French":
        dest="fr"
    elif lang_combo_value == "German":
        dest="de"
    elif lang_combo_value == "Spanish":
        dest="es"
    else:
        dest="en"
    result = translator.translate(INPUT, src=src_lang.lang, dest=dest)
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
clear_button.place(x=150, y=350)
trans_button = Button(button_frame, text="Translate", font=("Arial", 10, 'bold'), fg="#FFFFFF", bg="#303030", command=translate)
trans_button.place(x=290, y=350)
lang_combo = Combobox(button_frame, width=20, font=("Arial", 12))
lang_combo['values'] = ("English", "Vietnamese", "Japanese", "Chinese", "Korean", "French", "German", "Spanish")
lang_combo.place(x=150, y=310)
lang_combo.current(0)

# Create a text box
box_dest = Text(root, width=28, height=8, font=("ROBOTO", 16))
box_dest.pack(pady=80)

root.mainloop()
