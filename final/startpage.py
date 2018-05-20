from tkinter import *

import tkinter.ttk
root=Tk()

#=================turtle 1 =====================
def funct():
    import basic
btn=Checkbutton(root, text="beginner ", command=funct)
btn.grid( row =2 , column = 0, sticky="news")
#=================turtle 2 =====================

def funct2():
    import advanced
btn=Checkbutton(root, text="advance ", command=funct2)
btn.grid( row =2 , column = 1, sticky="news")

'''label1 =Label(root , text ="user name")
label1.grid(row =0 ,column = 0)
user_name=Entry(root)
user_name.grid(row =0, column = 1 )



label1 =Label(root , text ="password ")
label1.grid(row =1 ,column = 0)

user_name=Entry(root)
user_name.grid(row =1, column = 1)'''
root.mainloop()
