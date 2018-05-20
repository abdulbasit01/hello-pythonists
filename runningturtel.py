from tkinter import *


root=Tk()
def funct():
    import BothMoving.py
btn=Button(root, text="stat game", command=funct)
btn.grid()

root.mainloop()
