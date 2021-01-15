import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import random
import speech_recognition as sr
import pyjokes

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')

engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    #This function wishes user
    hour=int(datetime.datetime.now().hour)
    if(hour>=0 and hour<12):
        speak("Good Morning!")
    elif(hour>=12 and hour<18):
        speak("Good Afternoon!")
    else:
        speak("Good Evening !")
    speak("I m Jarvis  ! how can I help you sir")
def takecommand():
    #it takes user's command and returns string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        r.dynamic_energy_threshold=200
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language="en-in")
        print(f"User said {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query
exit_jarvis=False
if __name__ == '__main__':
    wishme()
    while not exit_jarvis:
     query=takecommand().lower()
     if 'wikipedia' in query:
        try:
         speak("Searching Wikipedia...")
         query=query.replace("wikipedia","")
         results=wikipedia.summary(query,sentences=4)
         speak("According to wikipedia")
         print(results)
         speak(results)
        except Exception as e:
            print(e)
            speak("Please connect your internet Sir")

     elif 'open youtube' in query:
         webbrowser.open("https://www.youtube.com/")
     elif 'open google' in query:
         webbrowser.open("https://www.google.com/")
     elif 'open github' in query:
         webbrowser.open("https://github.com/")
     elif 'open classroom' in query:
         webbrowser.open("https://classroom.google.com/u/1/h")
     elif 'open gmail' in query:
         webbrowser.open("https://mail.google.com/mail/u/0/#all")
     elif 'open college mail' in query:
         webbrowser.open("https://mail.google.com/mail/u/1/#inbox")
     elif 'play music' in query:
         music_dir= "D:\songs"
         songs=os.listdir(music_dir)
         a=random.randint(0,len(songs)-1)
         os.startfile(os.path.join(music_dir,songs[a]))
         print(songs)
     elif 'play video song' in query:
         video_dir= "D:\video songs"
         video=os.listdir(video_dir)

         b=random.randint(0,len(video)-1)
         os.startfile(os.path.join(video_dir,video[b]))
     elif 'time' in query:
         strtime=datetime.datetime.now().strftime('%H:%M:%S')
         speak(f'present time is {strtime}')
     elif 'open code block' in query:
         codepath="C:\CodeBlocks\\codeblocks.exe"
         os.startfile(codepath)
     elif 'bye' in query:
         speak("Thank you sir .Have a nice Day!")
         exit_jarvis=True
     elif 'joke' in query:
        speak(pyjokes.get_joke())
     elif 'spotify' in query:
         apppath=r"C:\Users\Jain\AppData\Local\Microsoft\WindowsApps\SpotifyAB.SpotifyMusic_zpdnekdrzrea0\\Spotify.exe"
         os.startfile(apppath)
     else:
         speak("Please repaeat sir what you are saying ,I dont understand it")






