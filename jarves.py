import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import os
import webbrowser
import sys
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishmenow():
    hour=(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good mornging dhivakar")
    elif hour>=12 and hour<18:
        speak("mathiya   vanakam   thalaiva")
    else:
        speak("good   evening   boss")
    speak("how   can   i   help   you")
    
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as mic:
        print("listening process....")
        r.pause_threshold=1.2
        audio=r.listen(mic)
        
    try:
        print("wait for few minutes")
        query=r.recognize_google(audio,language='en-in')
        print("user said", query)
    except Exception as e:
       
       speak("say that again please")
    
    
    if __name__ == "__main__":
        wishmenow()
    while True:
        query=takecommand().lower()
        if "wake up" in query:
            speak("I am On ,,,, please tell me what can i do ")
            while True:
                query = takecommand().lower()
                if 'wikipedia' in query:
                    speak('Searching in Wikipedia...')
                    query = query.replace("wikipedia", "")
                    results = wikipedia.summary(query, sentences=2)
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)
                elif 'log off ' in query or 'dolly log off pc' in query:
                    speak('okay')
                    os.system("shutdown /l /t 06")
                    speak('I am going to log of your computer Sir')
                    speak('Bye sir, have a good day.')
                    sys.exit()
                elif 'open youtube' in query:
                    webbrowser.open("youtube.com")
                elif 'open google' in query:
                    webbrowser.open("google.com")
                elif 'open stackoverflow' in query:
                    webbrowser.open("stackoverflow.com")
                elif 'play music' in query:
                    musicdir="G:\\SOnggg"
                    songs=os.listdir(musicdir)
                    print(songs)
                    os.startfile(os.path.join(musicdir,songs[16]))
                elif 'open code' in query:
                    codepath="C:\\Users\\Lokesh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                    os.startfile(codepath)
                elif 'open chrome' in query:
                    codepath1="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
                    os.startfile(codepath1)
                elif 'the time' in query:
                    time=datetime.datetime.now().strftime("%H:%M")
                    speak(time)
                elif 'quit' in query:
                    speak("quitting sir")
                    break
                elif 'exit' in query:
                    exit()
                        