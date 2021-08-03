import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
from googlesearch import search

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print (voices[1].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour= int(datetime.datetime.now().hour)
    if(hour>3 and hour<12):
        speak("good morning!!")
    elif(hour>=12 and hour<17):
        speak("good afternoon!!")
    elif(hour>=17 and hour<20):
        speak("good evening")
    else:
        speak("good night!!")
    speak("Hello, I'm Venessa . Please tell me how may I help you !!")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        r.pause_threshold =1                # to increase the time to listen before we end a statement
        audio=r.listen(source)

    try:
        print("Recognizing..")
        query=r.recognize_google(audio,language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        #print(e)
        print("Say that again please...")
        return "none"
    return query

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('your_email','your_email_password')
    server.sendmail('your_email',to,content)

if __name__ == '__main__':
    wishme()
    while True:
        query = takeCommand().lower()

        # logics for executing tasks based on query
        if 'wikipedia' in query:
            speak('searching wikipedia..')
            query=query.replace('wikipedia',"")                # replace the query with one word "wikipedia"
            results=wikipedia.summary(query, sentences=1)
            speak("according to wikipedia..")
            print(results)
            speak(results)

        elif 'google' in query:
            speak('searching google..')
            query = query.replace('google', "")                # wikipedia is not working so used google as option
            speak("following are the results")
            for j in search(query, tld="co.in", num=1):
                print(j)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'play music' in query:
            music_dir='C:\\Users\\Hp\\Music'                      # use of double slash as escape sequence
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[1]))        # changed to 1 as one extra file is there

        elif 'time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"mam,the time is {strTime}")

        elif 'vs code' in query:
            vspath="C:\\Program Files (x86)\\Microsoft Visual Studio\\2019\\Community\\Common7\\IDE\\devenv.exe"
            os.startfile(vspath)

        elif 'stop' in query:
            exit()

        elif 'email to me' in query:
            try:
                speak("what should I say?")
                content=takeCommand()
                to="singhdevsi943@gmail.com"
                sendEmail(to,content)
                speak("email has been sent!")
            except Exception as e:
                print(e)
                speak("sorry mam , I couldn't send this email!")
