from tkinter import *
from tkinter import filedialog
import winsound

class interface(Frame):
    def __init__(self, master):
        super(interface, self).__init__(master)
        self.grid()
        Photo = PhotoImage(file="Images-ViaDelMelodia/pure-black-background.png")
        Photo = Label(self, image=Photo)
        Photo.photo = Photo
        Photo.grid(row=0, column=0, rowspan=8,columnspan=7)
        self.selected = ""
        self.playing = True
        self.create_widgets()

    def choosethemusic(self):
        a = filedialog.askopenfile(initialdir="D:/", title='Choose Your WAV', filetypes=
        (("wav files", "*.wav"), ("all files", "*.*")))
        b = str(a)

        start = b.index("\'")
        b = b[int(start) + 1:]
        end = b.index("'")
        b = b[:int(end)]
        self.selected = b
        print(self.selected)

    def play_music(self):
        if self.playing == False:
            print("no play")
            winsound.PlaySound(None, winsound.SND_FILENAME)
            self.playing = True
        elif self.playing == True:
            print("Playing")
            winsound.PlaySound(self.selected, winsound.SND_ASYNC)
            self.playing = False
        if self.selected == False:
            Label(self, text = ":< it does not play ").grid(row = 8, column=3)
        elif self.selected == True:
            Label(self, text= "Aye it plays").grid(row=8, column =3)

    def create_widgets(self):
        Label(self, text="Via Del Melodia:", font=("Helvetica", 30, "bold")).grid(row=1, column=3)
        Label(self, text="Choose song below :D for reccomendations!!", font=("Helvetica", 15)).grid(row=4, column=3)

        choosebutton = Button(self, text="Choose File:", command=self.choosethemusic, font=("Helvetica", 10, "bold"))
        choosebutton.grid(row =5, column=1)

        playbutton = Button(self, text="Play Music/Stop Music", command=self.play_music,font=("Helvetica", 10, "bold")).grid(row =5, column = 4)

        Label(self, text="By Hayun Jung, Devon Lai, Kevin Liu", font=("Helvetica",16)).grid(row=7, column = 3)

root = Tk()
root.title("Via del Melodia")
app = interface(root)
root.mainloop()