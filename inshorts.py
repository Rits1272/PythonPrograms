from bs4 import BeautifulSoup
import requests
import html5lib
import pyttsx3
import time

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

URL = "https://inshorts.com/en/read"
response = requests.get(URL)
soup = BeautifulSoup(response.content, 'html5lib')
headlines = soup.findAll('span', attrs = {'itemprop' : 'headline'})
count_headlines = len(headlines)

speak("Welcome to audioShorts where you will get the Headlines of the inshorts news")
speak("Do you want subtitles for news?")

print("1 for Yes and 0 for No")
check = int(input())

if check != 0 and check != 1:
    speak("I do not understand your choice sir")
    exit()

speak("There are " + str(count_headlines) + 'headlines for today')
speak("How many do you want to listen?")
listen_count = int(input("No. of headlines?"))

if listen_count <= count_headlines and check is 1 or check is 0:
    for i in range(listen_count):
        speak('News number ' + str(i + 1))
        time.sleep(0.4)
        if check == 1:
            print("**** NEWS NUMBER " + str(i+1) + " ****")
            print(headlines[i].text)
            print("")
            speak(headlines[i].text)
            time.sleep(1)

        elif check == 0:
            speak(headlines[i].text)
            time.sleep(1)

else:
    speak("You are a dumbass")
