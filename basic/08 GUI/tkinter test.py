from tkinter import *

root = Tk()
root.title('App')
root.geometry("600x400")

label = Label(root, text="Quiz!", font="Courier 35", fg="yellow")
label.pack()

def click_action():
    print("Wow!")

click_button = Button(root, text="Click me!", width=8, bg="#ffb3fe", command=click_action)
click_button.pack()



root.mainloop()