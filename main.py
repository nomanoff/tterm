import speech_recognition as sr
import webbrowser
from time import ctime
from tkinter import *
import pyttsx3
from time import sleep



root = Tk()
root.title('Python Script')
root.geometry('800x500')


# we need a text display
display = Text(root, width=60, height=15)
display.bind("<Key>", lambda e: "break")
display.pack(pady=10)


# text on display
display_text = "Welcome To The Show"



# ALL COMMANDS

# empty command
def empty_command():
    global display_text
    display_text = "NO COMMAND HAS BEEN GIVEN"
    display.delete('1.0', END)
    display.insert(END, display_text)



# reads the display
def talk():                                                             
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty("rate", 180)
    engine.setProperty('voice', voices[1].id)
    engine.say(display.get("1.0", END))
    engine.runAndWait()


# shows the time
def time():
    global display_text
    display_text = ctime()
    display.delete('1.0', END)
    display.insert(END, display_text)


def location():
    global display_text
    display_text = "Where...?"
    display.delete('1.0', END)
    display.insert(END, display_text)
    my_entry.delete("0", END)
    talk()



def speak():

    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty("rate", 180)
    engine.setProperty('voice', voices[1].id)
    engine.say("Hi, how are you?")
    engine.runAndWait()


# Take the Input
my_entry = Entry(root, font=('Helvetica', 20))
my_entry.pack(pady=10)



def check_command(command):
    if command.get() == '':
        empty_command()

    if 'time' in command.get():
        time()

    if 'speak' in command.get():
        speak()

    if 'location' in command.get():
        location()


def check_command_caller(event):
    check_command(my_entry)


go_btn = Button(root, text="GO", command= lambda: check_command(my_entry))
root.bind('<Return>', check_command_caller)

go_btn.pack(pady=8)


read_btn = Button(root, text="READ", command=talk )
read_btn.pack(pady=8)


display.insert(END, display_text)


root.mainloop()