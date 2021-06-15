from tkinter import *

class Previous(Frame):
    def __init__(self,master, back):
        super().__init__(master)
        self.back = back
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Label(self, text="Previous Recommendations!!", font=("Helvetica", 30, "bold")).grid(row=1, column=3)
        Button(self, text="Go back for more Recommendations!", command=self.back,font=("Helvetica", 20, "bold")).grid(row=7, column = 3)

    def back(self):
        self.back()
