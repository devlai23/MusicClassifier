from tkinter import *
from tkinter import filedialog
import winsound
from SongRec import SongRec
from model import GenreClassifier
from threading import *

currentUser = None
pastrecs = []
selectedSong = None

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
        
        global selectedSong
        selectedSong = b
        self.selected = b


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
            Label(self, text = ":< it does not play ").grid(row = 8, column=4)
        elif self.selected == True:
            Label(self, text= "Aye it plays").grid(row=8, column =3)

    def create_widgets(self):
        back = PhotoImage(file="trial.png")
        w = Label(self, image=back)
        w.photo = back
        w.grid(column=0, rowspan=15, columnspan=30)
        Label(self, text="Choose song below :D for recommendations!!", font=("Helvetica", 15)).grid(row=0, column=2)

        Button(self, text="Choose File:", command=self.choosethemusic, font=("Helvetica", 10, "bold")).grid(row =7, column=2)

        Button(self, text="Play Music/Stop Music", command=self.play_music,font=("Helvetica", 10, "bold")).grid(row =7, column = 2)

        Button(self, text="Previous Recommendations", command=self.recommendations, font=("Helvetica", 10, "bold")).grid(row=8, column=2)

        Button(self, text="New Recommendation", command=self.threading, font=("Helvetica", 10, "bold")).grid(row=6, column=5)

        Label(self, text="By Hayun Jung, Devon Lai, Kevin Liu", font=("Helvetica",16)).grid(row=14, column = 3)

    def threading(self):
        t1 = Thread(target=self.n)
        t1.start()

    def recommendations(self):
        global currentUser 
        previoussongs = SongRec.retrieveSongs(currentUser)
        global pastrecs
        pastrecs = previoussongs
        self.previous()
    
    def getPastRecs(self):
        global pastrecs
        return pastrecs

    def n(self):
        Label(self, text="", font=("Helvetica", 10, "bold")).grid(row=11, column=3)
        # 1. send input song to ML model to determine genre
        global selectedSong
        g = GenreClassifier()
        out = g.predict(selectedSong)
        print(out.getTitle())

        
        # 2. run recommend function, using genre as input
        global currentUser
        ret = SongRec.recommend(out.getTitle(), currentUser)

        # display rec on screen instead of in terminal
        s = ""
        for x in ret:
            s += x + " "
        Label(self, text=s, font=("Helvetica", 10, "bold")).grid(row=11, column=3)

    def getSampleGenre(self,a):
        return "Country"