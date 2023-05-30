from selenium import webdriver
from bs4 import BeautifulSoup
from reader import *
from outside import *
from extract import *

tag_index = -1
tag_list = []

def start_chunkSR(link):
    say("Shall I provide a summary of the webpage contents?")
    choice = listen()
    if choice == "yes":
        get_contents(link)
        webpage_content = summarise()
        say(webpage_content)
        return
    else:
        read_webpage(link)
        return


