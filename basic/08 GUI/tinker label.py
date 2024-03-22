import tkinter as tk
import os

scriptDir = os.path.dirname(__file__)
os.chdir(scriptDir)

window = tk.Tk()
window.title("Application")
window.geometry('800x600')


logo = tk.PhotoImage(file="img2.png")

label1 = tk.Label(window,
                  text="Hello",
                  foreground="white",
                  background="green",
                  width=20,
                  height=3,
                  cursor="dot",
                  font= "Times 18 bold italic",
                  anchor= tk.CENTER,
                  padx= 5,
                  pady= 5
                  )
label1.pack(fill=tk.BOTH,side=tk.TOP, expand=True)

label2 = tk.Label(text="Hello again")
label2.pack(fill=tk.BOTH, expand=True)

label3 = tk.Label(window,
                  text="Test",
                  foreground="red",
                  image = logo,
                  compound=tk.CENTER)
label3.pack(fill=tk.BOTH,side=tk.BOTTOM, expand=True)

label3.config(text="Hello\nHello")


window.mainloop()

