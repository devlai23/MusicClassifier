from tkinter import *

class Up(Frame):
    def __init__(self, master, back):
        super().__init__(master)
        self.back = back
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        back = PhotoImage(file="kassy.png")
        w = Label(self, image=back)
        w.photo = back
        w.grid(row=0, column=0, rowspan=15, columnspan=8)
        self.user_var = StringVar()
        self.pass_var = StringVar()


        # Password
        Label(self, text="Password:", font=("Helvetica", 15)).grid(row=7, column=2)
        self.password = Entry(self, textvariable=self.pass_var,width=20)
        self.password.grid(row=8, column=2)

        # Username
        Label(self, text="Username:", font=("Helvetica", 15)).grid(row=5, column=2)
        self.username = Entry(self, textvariable=self.user_var, width=20)
        self.username.grid(row=6, column=2)

        # Next
        Button(self, text="Next", command=self.signup, font=("Helvetica", 18)).grid(row=9, column=2)

    def signup(self):
        users=open("users.txt", "r+")
        uarr = users.read().split()
        passes=open("passwords.txt", "r+")
        parr = passes.read().split()

        name = self.user_var.get()
        password = self.pass_var.get()

        users.write(name + " ")
        passes.write(password + " ")
        self.back()
