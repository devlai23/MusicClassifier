from tkinter import *
from interface import interface
from login_page import Login
from sign_in import In
from sign_up import Up
from previous import Previous

class Manager(object):
    def __init__(self):
        self.root = Tk()
        self.currentScreen = None

    def start_screen(self):
        self.root.title("Via Del Melodia")
        self.currentScreen = Login(self.root, self.sign_in, self.sign_up)
    def start(self):
        self.currentScreen.destroy()
        self.root.title("Via Del Melodia")
        self.currentScreen = Login(self.root, self.sign_in, self.sign_up)
    def sign_in(self):
        self.currentScreen.destroy()
        self.root.title("Sign In")
        self.currentScreen = In(self.root, self.interface)

    def sign_up(self):
        self.currentScreen.destroy()
        self.root.title("Sign Up")
        self.currentScreen = Up(self.root, self.start)

    ##def loading(self):
        ##self.root.geometry("1200x600")
        ##self.root.title("Via Del Melodia")
        ##self.currentScreen = Default(self.root)

    def interface(self):
        self.currentScreen.destroy()
        self.root.title("Choose Recommendations")
        self.currentScreen = interface(self.root, self.recommendations, In.getUser(self))

    def recommendations(self):
        self.currentScreen.destroy()
        self.root.title("Previous Recommendations")
        self.currentScreen = Previous(self.root, self.interface)

def main():
    music = Manager()
    music.start_screen()
    music.root.mainloop()


main()
