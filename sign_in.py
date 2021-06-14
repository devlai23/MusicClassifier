from tkinter import *

class In(Frame):
    def __init__(self, master):
        super(In, self).__init__(master)
        self.grid(row=0, column=0, rowspan=8,columnspan=7)
        self.create_widgets()

    def create_widgets(self):
        Label(self, text="Enter your password and username!!", font=("Helvetica", 30, "bold")).grid(row=1, column=3)

        # Password
        Label(self, text="Password", font=("Helvetica", 20)).grid(row=5, column=3)
        self.password = Entry(self)
        self.password.grid(row=6, column=3)

        # Username
        Label(self, text="Username", font=("Helvetica", 20)).grid(row=3, column=3)
        self.username = Entry(self)
        self.username.grid(row=4, column=3)
