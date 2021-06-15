from tkinter import *

class Up(Frame):
    def __init__(self, master, choosing):
        super().__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.user_var = StringVar()
        self.pass_var = StringVar()

        Label(self, text="Enter your password and username!!", font=("Helvetica", 30, "bold")).grid(row=1, column=3)

        # Password
        Label(self, text="Password", font=("Helvetica", 20)).grid(row=7, column=3)
        self.password = Entry(self, textvariable=self.pass_var)
        self.password.grid(row=9, column=3)

        # Username
        Label(self, text="Username", font=("Helvetica", 20)).grid(row=3, column=3)
        self.username = Entry(self, textvariable=self.user_var)
        self.username.grid(row=5, column=3)

        # Next
        Button(self, text="Next", command=self.signup, font=("Helvetica", 20)).grid(row=11, column=3)

    def signup(self):
        users=open("users.txt", "r+")
        uarr = users.read().split()
        passes=open("passwords.txt", "r+")
        parr = passes.read().split()

        name = self.user_var.get()
        password = self.pass_var.get()

        users.write(name + " ")
        passes.write(password + " ")