import requests
from bs4 import BeautifulSoup
import webbrowser
from selenium import webdriver
import re

cleanr = re.compile('<.*?>')

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiouy"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("e"):
        count -= 1
    if count == 0:
        count += 1
    return count


while True:
    almancaisim = input("Write a noun: ")

    dersite = "https://der-artikel.de/der/" + (almancaisim.title()) + ".html"
    diesite = "https://der-artikel.de/die/" + (almancaisim.title()) + ".html"
    dassite = "https://der-artikel.de/das/" + (almancaisim.title()) + ".html"

    r1 = requests.get(dersite)
    soup = BeautifulSoup(r1.content, 'html.parser')
    h1 = soup.find('h1')

    r2 = requests.get(diesite)
    soup = BeautifulSoup(r2.content, 'html.parser')
    h2 = soup.find('h1')

    r3 = requests.get(dassite)
    soup = BeautifulSoup(r3.content, 'html.parser')
    h3 = soup.find('h1')

    if syllable_count(almancaisim) < 2:

     if h2 == h3 != h1:
        print("----------")
        print("Nominativ:" + " " +"Der" + " " + (almancaisim.title()))
        print("----------")
        print("Akkusativ:" + " " + "Den" + " " + (almancaisim.title()))
        print("----------")
        print("Dativ:" + " " + "Dem" + " " + (almancaisim.title()))
        print("----------")
        print("Genitiv:" + " " + "Des" + " " + (almancaisim.title()) + "es")
        print("----------")

     elif h1 == h3 != h2:
        print("----------")
        print("Nominativ:" + " " + "Die" + " " + (almancaisim.title()))
        print("----------")
        print("Akkusativ:" + " " + "Die" + " " + (almancaisim.title()))
        print("----------")
        print("Dativ:" + " " + "Der" + " " + (almancaisim.title()))
        print("----------")
        print("Genitiv:" + " " + "Der" + " " + (almancaisim.title()))
        print("----------")
        

     elif h1 == h2 != h3:
        print("----------")
        print("Nominativ:" + " " + "Das" + " " + (almancaisim.title()))
        print("----------")
        print("Akkusativ:" + " " + "Das" + " " + (almancaisim.title()))
        print("----------")
        print("Dativ:" + " " + "Dem" + " " + (almancaisim.title()))
        print("----------")
        print("Genitiv:" + " " + "Des" + " " + (almancaisim.title()) + "es")
        print("----------")



    
    elif syllable_count(almancaisim) > int("1"):
     if h2 == h3 != h1:
        print("----------")
        print("Nominativ:" + " " +"Der" + " " + (almancaisim.title()))
        print("----------")
        print("Akkusativ:" + " " + "Den" + " " + (almancaisim.title()))
        print("----------")
        print("Dativ:" + " " + "Dem" + " " + (almancaisim.title()))
        print("----------")
        print("Genitiv:" + " " + "Des" + " " + (almancaisim.title()))
        print("----------")

     elif h1 == h3 != h2:
        print("----------")
        print("Nominativ:" + " " + "Die" + " " + (almancaisim.title()))
        print("----------")
        print("Akkusativ:" + " " + "Die" + " " + (almancaisim.title()))
        print("----------")
        print("Dativ:" + " " + "Der" + " " + (almancaisim.title()))
        print("----------")
        print("Genitiv:" + " " + "Der" + " " + (almancaisim.title()))
        print("----------")
        

     elif h1 == h2 != h3:
        print("----------")
        print("Nominativ:" + " " + "Das" + " " + (almancaisim.title()))
        print("----------")
        print("Akkusativ:" + " " + "Das" + " " + (almancaisim.title()))
        print("----------")
        print("Dativ:" + " " + "Dem" + " " + (almancaisim.title()))
        print("----------")
        print("Genitiv:" + " " + "Des" + " " + (almancaisim.title()))
        print("----------")

    elif almancaisim == "1":
        pass

    else:
        print("Noun couldn't find")

    tryagain = input('Do you want to search another noun (y/n)? ')

    if tryagain == "y":
        print("----------")

    elif tryagain == "Y":
        print("----------")

    elif tryagain == "n":
        print("Exiting...")
        break

    elif tryagain == "N":
        print("Exiting...")
        break
    else:
        print ("Exiting...")
        break












