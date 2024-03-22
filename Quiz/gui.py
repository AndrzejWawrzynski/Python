from tkinter import * 
from tkinter.ttk import *

root = Tk()
root.title('Quiz!:)')
root.geometry("400x400")

label1 = Label(root, text="Wpisz liczbe pytań (1 do 30)")
label1.grid(row = 0, column = 0, sticky = W, pady = 2)

label2 = Label(root, text="Wybierz język pytań :")
label2.grid(row = 1, column = 0, sticky = W, pady = 2)

label3 = Label(root, text="Wybierz poziom trudności :")
label3.grid(row = 2, column = 0, sticky = W, pady = 2)

number = 0
e1 = IntVar()
e1 = Entry(root)
e1.grid(row = 0, column = 1, pady = 2, padx = 10)

language = "Polish"
spin = IntVar()
def spinValue():
   spin = spin.get()
   
spin = Spinbox(root, from_ = 0,to = 1, values=("Polish", "English"), command=spinValue)
spin.grid(row = 1, column = 1, pady = 2)

level = "Easy"
spin2 = IntVar()
def spinValue2():
    spin2 = spin2.get()
    

spin2 = Spinbox(root, from_ = 0,to = 2, values=("Easy", "Medium", "Hard"), command=spinValue2)
spin2.grid(row = 2, column = 1, pady = 2)

def print_item_values():
    number = e1.get()
    language = spinValue()
    level = spinValue2()
    print(number, language, level)
    return number, language, level

value_button = Button(root, text = 'Print values', width = 10, command = print_item_values)
value_button.grid(row = 4, column = 0)


root.mainloop()