from tkinter import *

class Previous(Frame):
    def __init__(self,master, back, pastrecs):
        super().__init__(master)
        self.back = back
        self.grid()
        self.create_widgets(pastrecs)

    def create_widgets(self, pastrecs):
        Label(self, text="Previous Recommendations!!", font=("Helvetica", 30, "bold")).grid(row=1, column=3)
        lb = Listbox(self, width=40)
        for x in pastrecs:
            lb.insert('end', x)
        lb.grid(row=4, column = 3)

        Button(self, text="Go back for more Recommendations!", command=self.back,font=("Helvetica", 20, "bold")).grid(row=7, column = 3)

    def back(self):
        self.back()
