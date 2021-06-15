from selenium import webdriver
import random
from Song import Song

class SongRec:
    @staticmethod
    def retrieveSongs(user):
        songs = []
        acntinfo=open("acntinfo.txt", "r+")
        for line in acntinfo:
            if line.split("~")[0].strip() == user:
                info = line.split("~")
                for i in range(0, len(info)):
                    if i > 0:
                        songs.append(info[i].split(":")[0] + " by " + info[i].split(":")[1].strip())
        return songs

    @staticmethod
    def file_len(fname):
        with open(fname) as f:
            for i, l in enumerate(f):
                pass
            return i+1
        
    @staticmethod
    def recommend(input, user):
        acntinfo=open("acntinfo.txt", "r+")
        # genres = {}
        # for d in input.getConfidence().keys():
        #     if (d > threshold):
        #         genres[d] = input.getConfidence()[d]

        # max = -100
        # for x in input.getConfidence().keys():
        #     if x > max:
        #         max = x

        # genre = genres[max]
        if input == "hiphop":
            input = "hip" + chr(37) + "20hop"
        URL = "https://www.chosic.com/genre-chart/explore/?genre=" + input


        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)

        driver.get(URL)
        driver.implicitly_wait(15)
        try:
            frame = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/article[2]/div/div[1]/iframe')
        except:
            frame = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/article[3]/div/div[1]/iframe')
        
        driver.switch_to.frame(frame)
        songElement = driver.find_element_by_xpath('//*[@id="main"]/div/div/div[2]/div/table/tbody/tr[2]')
        songTitle = driver.find_element_by_css_selector('[dir]')
        attributes = songTitle.text.split("\n")

        rand = random.randint(1, 100)
        for i in range(0, len(attributes)):
            if (attributes[i] == str(rand)):
                song = attributes[i+1]
                artist = attributes[i+2]
                print("We recommend you", song, "by", artist)
                returnval = "We recommend you", song, "by", artist

        added = False
        counter = 0
        data = acntinfo.readlines()
        for line in data:
            if line.split("~")[0].strip() == user.strip():
                data[counter] = data[counter].strip() + "~" + song + ":" + artist + "\n"
                acntinfo.seek(0)
                acntinfo.truncate()
                
                acntinfo.writelines(data)
     
                added = True
            counter += 1
        if not added:
            acntinfo.write("\n" + user+"~"+song+":"+artist)

        driver.close()
        acntinfo.close()

        return returnval
# SongRec.recommend("country", "devon")

# users=open("users.txt", "r+")
# uarr = users.read().split()
# passes=open("passwords.txt", "r+")
# parr = passes.read().split()

# i=""
# user = None
# while (i != "quit"):
#     print("What would you like to do?")
#     i = input()
#     if (i == "sign up"):
#         print("please enter a username")
#         users.write(input() + " ")
#         print("please enter a password")
#         passes.write(input() + " ")

#     users.seek(0)
#     passes.seek(0)
#     uarr = users.read().split()
#     parr = passes.read().split()
#     while (i == "sign in"):
#         print("enter your username")
#         uin = input()
#         if (uin not in uarr):
#             print("invalid username")
#         else:
#             print("enter your password")
#             upass = input()
#             if (parr[uarr.index(uin)] == upass):
#                 user = uin
#                 break
#             else:
#                 print("invalid password")
#     if user != None:
#         break

# s = "Country"
# SongRec.recommend(s, user)