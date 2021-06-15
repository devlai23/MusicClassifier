from tkinter import *

username = None
class In(Frame):
    def __init__(self, master, choosing):
        super().__init__(master)
        self.choosing = choosing
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
        Button(self, text="Next", command=self.signin, font=("Helvetica", 20)).grid(row=11, column=3)

    def signin(self):
        users=open("users.txt", "r+")
        uarr = users.read().split()
        passes=open("passwords.txt", "r+")
        parr = passes.read().split()

        users.seek(0)
        passes.seek(0)
        uarr = users.read().split()
        parr = passes.read().split()

        name = self.user_var.get()
        password = self.pass_var.get()

        if name not in uarr:
            Label(self, text="Wrong Username, Try again!", font=("Helvetica", 20)).grid(row=11, column=5)

        else:
            Label(self, text="", font=("Helvetica", 20)).grid(row=11, column=5)
            if parr[uarr.index(name)] == password:
                global username
                username = name
                self.choosing()
            else:
                Label(self, text="Wrong Password, Try again!", font=("Helvetica", 20)).grid(row=11, column=5)

    def getUser(self):
        global username
        return username