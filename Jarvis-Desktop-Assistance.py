# Jarvis Desktop Assistance
import speech_recognition as sr
import datetime
import pyttsx3
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

# jarvis will speak
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# jarvis will wishme according to the time & introduce itself
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning!")
    elif hour>=12 and hour<=18:
        speak("Good Afternoon!")
    elif hour>=18 and hour<=21:
        speak("Good evening!")
    else:
        speak("Good Night!")
    
    speak(" How can i help you ")

#jarvis will take command
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(" Listining.......... ")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print(" Recognizing....... ")
        query = r.recognize_google(audio, language='en-IN')
        print(f' User said: {query}\n')

    except Exception as e:
        print(e)

        print(" Say that again please...... ")
        return "None"

    return query

#jarvis will send mails
def sendEmail(to,content):
    server = smtplib.SMTP('smntp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('senders_email','senders_psswd')
    server.sendmail('sender_email',to,content)
    server.close()

# to run the fuctions
if __name__ == "__main__":
    wishMe()

    while True:
        query = takeCommand().lower()

        #jarvis will perform function [wikipedia search]
        if 'wikipedia' in query:
            speak('Searching Wikipedia..... ')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query,sentences =2)
            speak(" According to wikipedia ")
            print(results)
            speak(results)

        #[open sites]
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            webbrowser.open('google.com')

        #[playing music]
        elif 'play music' in query:
            music_dir = 'F:\\songs'
            song = os.listdir(music_dir)
            print(song)
            os.startfile(os.path.join(music_dir,song[0]))

        #[time]
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime(" %H:%M:%S ")
            speak(f" The time is {strTime}")

        #[open softwares]
        elif 'open chrome' in query:
            path = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
            os.startfile(path)

        #[send email]
        elif 'email to me' in query:
            try:
                speak(" waht should i send")
                content = takeCommand()
                to ="deblinachakraborty785@gmail.com"
                sendEmail(to,content)
                speak(" email has been sent")
            except Exception as e:
                print(e)
                speak(" sorry i am not able to send the mail")

        
