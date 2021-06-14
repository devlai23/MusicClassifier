from tkinter import *
import random
class Default(Frame):
    root = Tk()
    root.title("Via del Melodia")
    myCanvas = Canvas(height=600, width=1200, bg = "black")
    myCanvas.pack(expand=YES, fill=BOTH)

    for i in range(30):
        r = random.randint(20,1170)
        myCanvas.create_line(20+r, 0, 20+r, 600, dash = (5, 2), fill = 'red')
    for i in range(90):
        x = random.randint(0,1170)
        y = random.randint(0,570)
        myCanvas.create_oval(x,y, x+25, y+25, fill = "white")

    widget = Label(myCanvas, text="Loading.....",font=("Helvetica",40), fg='white',bg='black')
    widget.pack()
    myCanvas.create_window(600, 300, window=widget)

    mainloop()