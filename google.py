from tkinter import * 
from PIL import Image,ImageTk
import googletrans
from distutils.dist import command_re
from googletrans import Translator
import pyttsx3
import speech_recognition



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


button_frame = Frame(root).pack(side = BOTTOM)




def clear():
    box.delete(1.0, END)
    box1.delete(1.0, END)
def translate():
    box1.delete(1.0,END)
    INPUT = box.get(1.0, END)
    t = Translator()
    a = t.translate(INPUT, dest = "en", src = "vi")
    b=a.text
    box1.insert(END, b)

def loa():
    loa = pyttsx3.init()
    loa.say(box1.get(1.0 , END))
    loa.runAndWait()

def mic():
    box.delete(1.0, END)
    box1.delete(1.0, END)
    mic = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as m:
        audio = mic.listen(m)
    try:
        box.insert(END,mic.recognize_google(audio,language="vi-VI"))
    except:
        box.insert(END,"")

 

clear_button = Button(button_frame , text = "Clear text", font=(("Arial"),10 , "bold"),bg = "#303030", fg = "#FFFFFF", command = clear)
clear_button.place(x = 150 , y = 310)
trans_button = Button(button_frame , text = "Translate", font=(("Arial"),10 , "bold"),bg = "#303030", fg = "#FFFFFF",command = translate)
trans_button.place(x = 290 , y = 310)

loa_button = Button(button_frame , text = "Loa", font=(("Arial"),10 , "bold"),bg = "#303030", fg = "#FFFFFF",command = loa)
loa_button.place(x = 430 , y = 520)

mic_button = Button(button_frame , text = "Mic", font=(("Arial"),10 , "bold"),bg = "#303030", fg = "#FFFFFF",command = mic)
mic_button.place(x = 430 , y = 90)

box1 = Text(root , width = 28 , height = 8 , font=("ROBOTO",16))
box1.pack(pady = 50)

root.mainloop()