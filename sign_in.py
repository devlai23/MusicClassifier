from tkinter import *

class In(Frame):
    def __init__(self, master, choosing):
        super().__init__(master)
        self.choosing = choosing
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Label(self, text="Enter your password and username!!", font=("Helvetica", 30, "bold")).grid(row=1, column=3)

        # Password
        Label(self, text="Password", font=("Helvetica", 20)).grid(row=7, column=3)
        self.password = Entry(self)
        self.password.grid(row=9, column=3)

        # Username
        Label(self, text="Username", font=("Helvetica", 20)).grid(row=3, column=3)
        self.username = Entry(self)
        self.username.grid(row=5, column=3)

        # Next
        Button(self, text="Next", command=self.choose, font=("Helvetica", 20)).grid(row=11, column=3)

    def choose(self):
        self.choosing()
