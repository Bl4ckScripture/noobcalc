from tkinter import *
from tkinter import Tk, Entry

# I wanted to change the font of the widgets but idk how to ¯\_(ツ)_/¯

# base
main: Tk = Tk()
main.geometry('300x105')
main.configure(bg='#2b2f34')
main.title('calculate')

# first label
lbl1 = Label(main, text='Input', bg='#2b2f34', fg='white')
lbl1.config(anchor=CENTER)
lbl1.pack()

# first entry
entry1: Entry = Entry()
entry1.pack()

outputbox = Text(main, height=1, width=18)
outputbox.pack()

def Clear():
    entry1.delete(0, 'end')
    outputbox.delete("1.0", 'end')

def Evaluate():
    return eval(str(entry1.get()))

def Calculate():
    outputbox.insert("1.0", Evaluate())

clear_button = Button(main, text='Clear', bg='#2b2f34', fg='white', command=Clear)
clear_button.config(anchor=CENTER)
clear_button.pack()

calculate_button = Button(main, text='Calculate', bg='#2b2f34', fg='white', command=Calculate)
calculate_button.config(anchor=CENTER)
calculate_button.pack()

main.mainloop()
