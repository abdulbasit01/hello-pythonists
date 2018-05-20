from tkinter import *
from tkinter.messagebox import *
import sys
import os
class LoginFrame(Frame):
    def __init__(self, master):
        super().__init__(master)
        
        self.label_header=Label(self ,text="if you have an account then login below", font=("Helviteca", "18", "bold italic"))
        self.label_header.grid(row=4,columnspan=3)
        
        self.label_top=Label(self ,text="Login Page" , font=("Helviteca", "24", "bold italic"))

        self.label_username = Label(self, font=("Times", "16", "bold italic"),text="Username",relief="ridge")
        self.label_password = Label(self,font=("Times", "16", "bold italic"), text="Password ",relief="ridge")
        self.label_top.grid(row=3, column=1)
        self.entry_username = Entry(self,relief="sunken",fg="white", bg="black", font=("Times", "16", "bold italic"))
        self.entry_password = Entry(self, show="@",relief="groove",fg="white", bg="black", font=("Times", "16", "bold italic"))
        
        self.label_username.grid(row=5, sticky=E)
        self.label_password.grid(row=10, sticky=E)
        self.entry_username.grid(row=5, column=1)
        self.entry_password.grid(row=10, column=1)

        self.logbtn = Button(self, text="Login", font=("Times", "16", "bold italic"),relief="raised",command=self._login_btn_clicked)
        self.logbtn.grid(columnspan=2)

        
        self.pack(side="right",fill="both")

    def _login_btn_clicked(self):
        # print("Clicked")
        username = self.entry_username.get()
        password = self.entry_password.get()

        # print(username, password)

        if (username == "abdulbasit@turtle.com" or "hadi@turtle.com" or "sanaullah@turtle.com" or "hamza@turtle.com" or "zubair@turtle.com") and password == "mahi":
            showinfo("Login info", "Welcome")
            
            import startpage
            
            
        else:
            showerror("Login error", "Incorrect username or empty fields")

root = Tk()

lf = LoginFrame(root)
root.title("login page",)
root.geometry("450x580")
root.configure(bg='peru')


root.mainloop()
