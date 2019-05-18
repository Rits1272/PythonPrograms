import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser

#  SAPI - Speech Application Programming Interface
#  The Speech Application Programming Interface or SAPI is an API developed by Microsoft
#  to allow the use of speech recognition and speech synthesis within Windows applications.
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

#  This function use sapi5 for converting text into speech.
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#  This function wishes you according to time.
def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour <= 12:
        speak("Good Morning Sir")
    elif hour >= 12 and hour <= 18:
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening Sir")

    speak("I am Jarvis at your service")

def takeCommand():
    '''
    Takes microphone input from the user and returns text output
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 200
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print("You said : ")
        print(query)

    except Exception as e:
        print("Say that again please..!")
        return "None"
    return query

#  send_email function uses smtplib which is an inbuilt
#  package in python to send email through gmail

if __name__ == '__main__':
    wishMe()
    query = takeCommand().lower()

    #  Login for executing task according to query.

    if 'wikipedia' in query:
    	speak("Searching wikipedia...")
    	query = query.replace("Wikipedia","")
    	results = wikipedia.summary(query, sentences = 2)
    	speak("According to wikipedia")
    	print(results)
    	speak(results)

    elif 'open youtube' in query:
   		webbrowser.open('youtube.com')

    elif 'open stackoverflow' in query:
    	webbrowser.open('stackoverflow.com')

    elif 'open google' in query:
        webbrowser.open('google.com')

    elif 'the time' in query:
    	strTime = datetime.datetime.now().strftime("%H:%M:%S")
    	speak("The time is : ")
    	speak(strTime)


    if 'stop' in query or 'quit' in query or 'exit' in query:
        speak("Exiting sir You are awesome Have a great day")
        exit()

    else:
        query = takeCommand().lower()
