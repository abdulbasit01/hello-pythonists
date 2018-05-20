from tkinter import *
import tkinter.ttk
class turtle(object):
    def __init__(self):
        self.pack()
        self.bind()
        self.create_Widgets()
    def create_Widgets(self):
        button=Button(self, text='none', command= self.newpage)
        self.button.grid()
   
root=Tk()
root.mainloop()
