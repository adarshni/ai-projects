import pyaudio
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import os
import webbrowser
import smtplib

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()
    
def takecommand():
    l=sr.Recognizer()
    #it takes microphone input and returns string o/p.
    with sr.Microphone() as source:
        print("listening...")
        l.pause_threshold=1
        voice=l.listen(source)
    try:
        print("Recognizing...")
        command=l.recognize_google(voice)  
        command=command.lower()
        print(f"user said: {command}")
    except Exception as e:
        print("say that again please..")
        return "none"
    return command

def sendemail(to,content):
    server=smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your email@gmail.com','passwd of ur mail')
    server.sendmail('your mail@gmail.com', to, content)
    server.close()
    

def quitSelf(): 
        talk("do u want to switch off the computer sir") 
  
        # Input voice command  
        take = takecommand() 
        choice = take 
        if choice == 'yes': 
  
            # Shutting down 
            print("Shutting down the computer") 
            talk("Shutting the computer") 
            os.system("shutdown /s /t 30") 
        if choice == 'no': 
  
            # Idle 
            print("Thank u sir") 
            talk("Thank u sir") 

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        talk("Good Morning")
    elif hour>=12 and hour<17:
        talk("Good afternoon")
    elif hour>=17 and hour<20:
        talk("good evening")
    else:
        talk("good night")
    talk("I am jarvis sir! please tell me how may i help u")
    

        
#talk("adarsh is a good boy")
wishme()
if 1:
    command=takecommand()
    if 'wikipedia' in command:
        talk("Searching wikipedia")
        command=command.replace("wikipedia","")
        command=command.replace("search","")
        result=wikipedia.summary(command,sentences=2)
        talk("according to wikipedia")
        print(result)
        talk(result)
    elif 'time' in command:
        time=datetime.datetime.now().strftime('%H:%M %p')
        print(time)
        talk(time)
    elif 'shutdown' in command:
        quitSelf()
    
    
    elif 'open' in command:
        command=command.replace("open ","")
        webbrowser.open('www.'+command+".com")
    elif 'play music' in command:
        music_dir='C:\\Users\\adars\\Music'
        song=os.listdir(music_dir)
        print(song)
        os.startfile(os.path.join(music_dir,song[3]))
    elif 'youtube' in command:
        song=command.replace('play','')
        talk('playing'+song)
        pywhatkit.playonyt(song)
    elif 'pycharm' in command:
        path="C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.3.2\\bin\\pycharm64.exe"
        os.startfile(path)
    elif 'email' in command:
        try:
            talk("what should i say")
            content=takecommand()
            to="1230@gmail.com"
            sendemail(to,content)
            talk("email has been sent")
        except Exception as e:
            print(e)
            talk("sorry my friend adarsh i m not able to send mail at moment")
    else:
        talk("jarvis here. hey sir plz tell me wht can i do for u.")
        command=takecommand()
        if 'bye' in command:
            talk("bye sir! have a good day")
            exit()
        else:
            talk("tell me sir jarvis here")
            
   
            
    
