from tkinter import *
from tkinter import filedialog
import winsound
from SongRec import SongRec

currentUser = None
pastrecs = []

class interface(Frame):
    def __init__(self, master, previous, user):
        global currentUser
        currentUser = user
        super().__init__(master)
        self.grid()
        self.selected = ""
        self.playing = True
        self.previous = previous
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

        playbutton = Button(self, text="Play Music/Stop Music", command=self.play_music,font=("Helvetica", 10, "bold")).grid(row =5, column = 5)

        previousbutton = Button(self, text="Previous Recommendations", command=self.recommendations, font=("Helvetica", 10, "bold")).grid(row=5, column=3)

        recommendations = Button(self, text="New Recommendation", command=self.next, font=("Helvetica", 10, "bold")).grid(row=6, column=5)

        Label(self, text="By Hayun Jung, Devon Lai, Kevin Liu", font=("Helvetica",16)).grid(row=8, column = 3)

    def recommendations(self):
        # define user variable
        # display songs on screen instead of in terminal
        global currentUser 
        previoussongs = SongRec.retrieveSongs(currentUser)
        global pastrecs
        pastrecs = previoussongs
        self.previous()
    
    def getPastRecs(self):
        global pastrecs
        return pastrecs

    def next(self):
        # 1. send input song to ML model to determine genre
        # 2. run recommend function, using genre as input
        # define both variables
        # display rec on screen instead of in terminal
        SongRec.recommend(genre, user)
        Label(self, text="Recommendation", font=("Helvetica", 10, "bold")).grid(row=7, column=3)
