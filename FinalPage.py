from tkinter import *
import string
import random
import os
#import sheets
from PIL import Image,ImageTk


path = "C:\\Users\\sjkadam\\MY_FINAL_PROJECT\\resources\\"

window = Tk()
window.title('Hand Gesture Controlled System')
window.iconbitmap(path + 'hand.png')
window.configure(background = "black")


heading = Label(window, text = 'Hand Gesture Controlled System', bg = "black", fg = "white",font = "Perpetua 24 bold")
heading.grid(row = 0,column = 0)

frame = LabelFrame(window,padx = 100, pady = 50)
frame.grid(padx = 10, pady = 10)
frame.configure(background = "white")

deathwing = Image.open(path + 'logo.png')
image = deathwing.resize((300,300),Image.ANTIALIAS)
Deathwing = ImageTk.PhotoImage(image)
imagelabel = Label(frame,image = Deathwing,borderwidth = 0)
imagelabel.grid(row = 0,column = 0)


def click():
    window2 = Tk()
    window2.title('Camera')
    # window2.iconbitmap(path + 'hand.png')
    heading = Label(window2, text='Thank You!', bg="black", fg="white", font="Perpetua 24 bold")
    heading.grid(row=0, column=0)

    frame = LabelFrame(window2, padx=100, pady=50)
    frame.grid(padx=20, pady=20)
    frame.configure(background="white")
    window2.configure(background="black")

    btn = Button(window2, text='Close me!', bg="gray", fg="white", height=1, width=20, command=window.quit)
    btn.grid(row=25, column=0, pady=10, padx=10)

    os.system('python "sheets.py"')


def click_start():
    window.destroy()



    root = Tk()
    root.title('User')
    #root.iconbitmap(path + 'logo.png')
    root.configure(background="black")

    new_frame = LabelFrame(root, padx=100, pady=80)
    new_frame.grid(padx=15, pady=15)
    new_frame.configure(background="white")

    labelG1= Label(new_frame, text="Palm : Open Notepad++", bg="white", pady=5, font="Perpetua 15 ")
    labelG1.grid(row=0, column=0, sticky='w')
    labelG2 = Label(new_frame, text="Scissor : open Powerpoint ", bg="white", pady=5, font="Perpetua 15 ")
    labelG2.grid(row=5, column=0, sticky='w')
    labelG3 = Label(new_frame, text="Right : Open WhatsApp ", bg="white", pady=5, font="Perpetua 15 ")
    labelG3.grid(row=10, column=0, sticky='w')
    labelG4 = Label(new_frame, text="Y : Open Google Chrome", bg="white", pady=5, font="Perpetua 15 ")
    labelG4.grid(row=15, column=0, sticky='w')
    labelG5 = Label(new_frame, text="fist: Open Paint", bg="white", pady=5, font="Perpetua 15 ")
    labelG5.grid(row=20, column=0, sticky='w')
    labelG6 = Label(new_frame, text="down: Open Adobe Acrobat Document Reader", bg="white", pady=5, font="Perpetua 15 ")
    labelG6.grid(row=25, column=0, sticky='w')


    btn = Button(new_frame, text='Click me !', bg="gray", fg="white", height=1, width=20, command=click)
    btn.grid(row=30, column=0, pady=10, padx=10)

start_image = PhotoImage()
start_button = Button(frame, image=start_image, command=click_start, height=40, width=300, bg="gray", borderwidth=0)
start_button.image = start_image
start_button.grid(row=2,column=0, padx=100, pady=10)
'''import sheets
def click():
# Calls the function play() file from sheets.py
    root.destroy()
    gesture = sheets.play()
    click(gesture)

pickup_button = Button(frame, command=click, height=230, width=290, bg="white", borderwidth=0)
pickup_button.grid(row=0, column=0)'''



window.mainloop()