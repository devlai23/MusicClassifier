from tkinter import *

class Login(Frame):
    def __init__(self, master, one, two):
        super(Login, self).__init__(master)
        self.grid(row=0, column=0, rowspan=8,columnspan=7)
        self.one = one
        self.two = two
        self.create_widgets()

    def create_widgets(self):
        Label(self, text = "Welcome to Via Del Melodia!!", font=("Helvetica", 30, "bold")).grid(row=1, column=3)
        Button(self, text="Login",command=self.sign_in, font=("Helvetica", 10, "bold")).grid(row =5, column = 4)
        Button(self, text="Sign in",command=self.sign_up, font=("Helvetica", 10, "bold")).grid(row =5, column=1)

    def sign_in(self):
        self.one()

    def sign_up(self):
        self.two()