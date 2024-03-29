from tkinter import *

okno=Tk()
okno.title("Powitanie")
lista=[]
 
def zatwierdz(label):
    def show_text():
        dane1=a.get()
        dane2=b.get()
        imnz=dane1+" "+dane2
        lista.append(imnz)
        label.config(text="Witaj "+imnz)
 
    return show_text
 
a=StringVar()
b=StringVar()
Label(text="Podaj swoje imie :") .grid(row=0,column=0)
Entry(textvariable=a).grid(row=0, column=1)
Label(text="Podaj swoje Nazwisko :") .grid(row=1,column=0)
Entry(textvariable=b).grid(row=1, column=1)
result_label = Label(okno, text="")
result_label.grid(row=4, column=0)
button_command = zatwierdz(result_label)
Button(text="Zatwierdź", command=button_command).grid(row=2,column=0)
okno.mainloop()
 