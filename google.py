#Thêm các thứ viện cần thiết cho chường trình
from random import lognormvariate
from tkinter import * 
from PIL import Image,ImageTk
import googletrans
from distutils.dist import command_re
from googletrans import Translator
import pyttsx3
import speech_recognition
import tkinter as tk
from tkinter import ttk


def clear():
    box.delete(1.0, END)
    box1.delete(1.0, END)

#vi en fr ko ja
def chuyen():
    vao = capnhat()[2]
    ra = capnhat()[3]
    combov.current(ra)
    combor.current(vao)
    temp =  box.get(1.0, END)
    temp1 =  box1.get(1.0, END)
    box.delete(1.0, END)
    box1.delete(1.0, END)
    box.insert(END, temp1)
    box1.insert(END, temp)
    
def capnhat():
    lv = combov.get()
    lr = combor.get()
    if lv == "Việt" :
        lv = 'vi'
        vao = 0
    elif lv == "Anh":
        lv = 'en'
        vao = 1 
    elif  lv == "Pháp":
        lv = "fr"
        vao = 2
    elif lv == "Hàn":
        lv = 'ko'
        vao = 3
    else:
        lv = 'ja'
        vao = 4
    if lr == "Việt" :
        lr = 'vi'
        ra = 0
    elif lr == "Anh":
        lr = 'en'
        ra = 1
    elif  lr == "Pháp":
        lr = "fr"
        ra = 2
    elif lr == "Hàn":
        lr = 'ko'
        ra = 3
    else:
        lr = 'ja'
        ra = 4
    return lv , lr , vao , ra
def translate():
    lv = capnhat()[0]
    lr = capnhat()[1]
    box1.delete(1.0,END)
    INPUT = box.get(1.0, END)
    t = Translator()
    a = t.translate(INPUT, dest = lr, src = lv)
    b=a.text
    box1.insert(END, b)

def loa():
    loa = pyttsx3.init()
    loa.say(box1.get(1.0 , END))
    loa.runAndWait()

def mic():
    clear()
    mic = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as m:
        audio = mic.listen(m)
    try:
        box.insert(END,mic.recognize_google(audio,language= lv))
    except:
        box.insert(END,"")


root = Tk()
root.title("Google Dịch")
root.geometry("500x630")
root.iconbitmap("logo.ico")



load = Image.open("background.png")
render = ImageTk.PhotoImage(load)
img = Label(root , image = render)
img.place(x = 0 , y = 0)




name = Label(root , text = "Translator" , fg = "#FFFFFF" , bd = 0, bg ="#02142C")
name.config(font = ("Transformers Movie",30))
name.pack(pady=10)



box = Text(root , width = 28 , height = 8 , font=("ROBOTO",16))
box.pack(pady = 20)


box1 = Text(root , width = 28 , height = 8 , font=("ROBOTO",16))
box1.pack(pady = 50)

button_frame = Frame(root).pack(side = BOTTOM)

vao = 0
combov = ttk.Combobox(root, width = 28, height = 8,  textvariable =tk.StringVar()) 
combov['values']= ("Việt", "Anh", "Pháp","Hàn", "Nhật")
combov.current(vao)
combov.place(x = 80 , y = 65, width = 340, height = 20)

ra = 1
combor = ttk.Combobox(root, width = 28, height = 8,  textvariable =tk.StringVar()) 
combor['values']= ("Việt", "Anh", "Pháp","Hàn", "Nhật")
combor.current(ra)
combor.place(x = 80 , y = 330, width = 340, height = 20)

lv = ""
lr = ""


clear_button = Button(button_frame , text = "Clear text", font=(("Arial"),10 , "bold"),bg = "#303030", fg = "#FFFFFF", command = clear)
clear_button.place(x = 120 , y = 300)

trans_button = Button(button_frame , text = "Translate", font=(("Arial"),10 , "bold"),bg = "#303030", fg = "#FFFFFF",command = translate)
trans_button.place(x = 310 , y = 300)

chuyen_button = Button(button_frame , text = "Chuyển", font=(("Arial"),10 , "bold"),bg = "#303030", fg = "#FFFFFF",command = chuyen)
chuyen_button.place(x = 220 , y = 300)

loa_button = Button(button_frame , text = "Loa", font=(("Arial"),10 , "bold"),bg = "#303030", fg = "#FFFFFF",command = loa)
loa_button.place(x = 430 , y = 520)

mic_button = Button(button_frame , text = "Mic", font=(("Arial"),10 , "bold"),bg = "#303030", fg = "#FFFFFF",command = mic)
mic_button.place(x = 430 , y = 90)



root.mainloop()