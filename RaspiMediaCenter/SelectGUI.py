from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
from subprocess import call
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

root = tk.Tk()
root.geometry("960x800")
def driver():
    pass
    #driver = webdriver.Chrome('./chromedriver')
def NetflixButtonPressed():
    driver = webdriver.Chrome('./chromedriver')
    print("NETFLIX PRESSED")
    driver.get("https://www.netflix.com")
    print(driver.title)
    search_bar = driver.find_element_by_name("q")
    search_bar.clear()
    #search_bar.send_keys("getting started with python")
    #search_bar.send_keys(Keys.RETURN)
    #print(driver.current_url)
    driver.close()

def DisneyButtonPressed():
    driver = webdriver.Chrome('./chromedriver')
    print("DISNEYPLUS Pressed")
    driver.get("https://www.disneyplus.com/")
    print(driver.title)
    search_bar = driver.find_element_by_name("login")
    search_bar.clear()
    #search_bar.send_keys("getting started with python")
    #search_bar.send_keys(Keys.RETURN)
    #print(driver.current_url)
    driver.close()

def shutdownraspi():
    call("sudo nohup shutdown -h now", shell=True)

canvas = Canvas(root, width=500, height=500)
canvas.pack()

#add images

Netflix = ImageTk.PhotoImage(Image.open("NetflixLogo.png"))
DisneyPlus = ImageTk.PhotoImage(Image.open("DisneyPlusLogo.jpg"))
OFF = ImageTk.PhotoImage(Image.open("PowerButton3.png"))

NetflixButton = Button(root,  height=160, width=600, text="", image=Netflix,command=lambda: NetflixButtonPressed())
NetflixButton.place(x=100,y=30)

DisneyButton = Button(root,  height=300, width=600, text="", image=DisneyPlus,command=lambda: DisneyButtonPressed())
DisneyButton.place(x=100,y=200)

OffButton = Button(root,  height=250, width=250, text="", image=OFF,command=lambda: shutdownraspi())
OffButton.place(x=700,y=600)


root.mainloop()
