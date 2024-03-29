from tkinter import *
import quiz

root = Tk()
root.geometry("800x600")
root.title("Quiz ver.001")

label1 = Label(root, text="Wpisz liczbe pytań :", font=("Helvetica", 20))
label1.grid(row = 0, column = 0,  sticky = W, pady = 2)

label2 = Label(root, text="Wybierz język pytań :", font=("Helvetica", 20))
label2.grid(row = 1, column = 0, sticky = W, pady = 2)

label3 = Label(root, text="Wybierz poziom trudności :", font=("Helvetica", 20))
label3.grid(row = 2, column = 0, sticky = W, pady = 2)

# def grab
number = 10
language = "Polish"
level = "Easy"
def grab():
    global language, level, number
    language = spin1.get()
    level = spin2.get()
    number = spin.get()
    label5.config(text="liczba pytan - " + str(number) +
                  " : " + "jezyk - " + language + 
                  " : " + " poziom - " + level, 
                  fg="yellow", font=("Helvetica", 20))
    
# def questions
def questions():
    label6.config(text="", font=("Helvetica", 20))
    
# Spin Number
n = (1,5,10,15,20,25,25,30)
spin = Spinbox(root, values=n, font=("Helvetica", 20))
spin.grid(row = 0, column = 1, pady = 2, padx = 10)

# Spin1 Language
spin1Values = ("Polish", "English")
spin1 = Spinbox(root, values=spin1Values, font=("Helvetica", 20))
spin1.grid(row = 1, column = 1, pady = 2)

# Spin2 Level
spin2Values = ("Easy", "Medium", "Hard")
spin2 = Spinbox(root, values=spin2Values, font=("Helvetica", 20))
spin2.grid(row = 2, column = 1, pady = 2)

# Button1
button1 = Button(root, text="Akccept", font=("Helvetica", 20),command=grab)
button1.grid(row = 3, column = 1, pady = 2)


# label wybrano zawartosc
label5 = Label(root, text=" ")
label5.grid(row = 4, columnspan = 3, sticky=W, pady = 2)

# Button2
button2 = Button(root, text="Start", font=("Helvetica", 20), command=questions)
button2.grid(row = 5, column = 1, pady = 2)

# lista
quiz.Quiz(number)
quiz.level = level
quiz.language = language
listQuestions = quiz.qL

# text lista
label6 = Label(root, text= quiz.qL)
label6.grid(rowspan= 3, columnspan=2, sticky=W, pady= 2)


if __name__ == "__main__":
    root.mainloop()