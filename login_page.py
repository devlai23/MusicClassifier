from tkinter import *
class Login(Frame):
    def __init__(self, master, one, two):
        super(Login, self).__init__(master)
        self.one = one
        self.two = two
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        back = PhotoImage(file="creditscreen.png")
        w = Label(self, image=back)
        w.photo = back
        w.grid(row=0, column=0, rowspan=16, columnspan=16)
        Label(self, text = "Welcome to Via Del Melodia!!", font=("Helvetica", 30, "bold")).grid(row=0, column=4)
        Button(self, text="Sign in",command=self.sign_in, font=("Helvetica", 20, "bold")).grid(row =7, column = 1)
        Button(self, text="Sign up",command=self.sign_up, font=("Helvetica", 20, "bold")).grid(row =7, column=6)

    def sign_in(self):
        self.one()

    def sign_up(self):
        self.two()