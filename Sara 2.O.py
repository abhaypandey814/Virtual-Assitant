import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import pyaudio

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[1].id)              #from here we can change the voice from male to female

def speak(audio):
    engine.say(audio)
    engine.runAndWait()                                    #without this command, speech will not be audible to us.

def wishMe():
    hour = int(datetime.datetime.now().hour)            #according to the timing the AI will wish you 
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Goof Afternoon!")
    else:
        speak("Good Evening!")

    speak("Hello I am Sara 2.0 .How can I help you?")
   #here what will we write the same thing will be read by the software
def takeCommand():
    #it takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:           #from here the AI will understand the instruction given by the user.
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')              #HERE exception handling has been used 
        print(f"User said: {query}")

    except Exception as e:

        print("Say that again please....")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.startt1s()
    server.login('youremail@gmail.com', 'your-password-here')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__== "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

    # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open hackerrank' in query:
            webbrowser.open("hackerrank.com")
        elif 'open spotify' in query:
            webbrowser.open("spotify.com")
        elif 'open github' in query:
            webbrowser.open("github.com")
        elif 'open notepad++' in query:
            codePath="C:\\Program Files\\Notepad++\\notepad++.exe"
            os.startfile(codePath)

        elif 'the time' in query:
            strTime= datetime.datetime.now().strftime("%H:%H:%S")
            speak(f"Sir, the Time is {strTime}")

        elif 'email to abhay' in query:
            try:
                speak("What should I say?")
                content=takeCommand()
                to="pandeyabhay0686@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend Abhay bhai. I am not able to send email")