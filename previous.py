from tkinter import *

class Previous(Frame):
    def __init__(self,master, back, pastrecs):
        super().__init__(master)
        self.back = back
        self.grid()
        self.create_widgets(pastrecs)

    def create_widgets(self, pastrecs):
        back = PhotoImage(file="acourve.png")
        w = Label(self, image=back)
        w.photo = back
        w.grid(row=0, column=0, rowspan=15, columnspan=8)
        Label(self, text="Previous Recommendations!!", font=("Helvetica", 18)).grid(row=0, column=3)
        lb = Listbox(self, width=50)
        for x in pastrecs:
            lb.insert('end', x)
        lb.grid(row=3, column = 3)

        Button(self, text="Go back for more Recommendations!", command=self.back,font=("Helvetica", 10, "bold")).grid(row=1, column = 3)

    def back(self):
        self.back()
