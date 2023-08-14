import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib,ssl
import openai
from config import apikey
import random
 

engine = pyttsx3.init('sapi5')
voices = engine.getProperty("voices")
# print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def Wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good morning sir")
    elif hour>=12 and hour<=16:
        speak("Good afternoon sir")
    else:
        speak("Good evening sir")
    speak("I am jarvis sir. How may I help you")

def takeCommand():
    #it takes microphone input from user and gives output as string

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning....")
        r.pause_threshold= 0.8
        audio=r.listen(source)
    
    try:
        print("Recognizing....")
        query=r.recognize_google(audio,language="en-in")
        print(f"user said :{query}\n")
    except Exception as e:
        print(e)
        print("Say that again please..")
        return "none"
    return query

def sendEmail(to,content):
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login("sender@gmail.com","password")
    server.sendmail("sender@gmail.com",to,content)
    server.close()
    
def ai(prompt):
    openai.api_key = apikey
    text=f"OpenAI responce for {prompt}:\n"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=1,
        max_tokens=256,
        top_p=1,    
        frequency_penalty=0,
        presence_penalty=0
    )
    
    # print(response["choices"][0]["text"])
    text += response["choices"][0]["text"]
    i=1
    if not os.path.exists("openai"):
        os.mkdir("openai")
    with open(f"openai/{''.join(prompt.split('intelligence')[1:])}-{i}.txt","w") as f:
        f.write(text)
    i=i+1

charStr=""
def chat(query):
    global charStr
    
    openai.api_key = apikey
    charStr+= f"Mastar:{query}\nJarvis: "
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=charStr ,
        temperature=1,
        max_tokens=256,
        top_p=1,    
        frequency_penalty=0,
        presence_penalty=0
    )
    
    speak(response["choices"][0]["text"])
    charStr+= f"{response['choices'][0]['text']}\n"
    print(charStr)
    return response['choices'][0]['text']
   
  
if __name__=="__main__":
    Wishme() 

    while True:
        query = takeCommand().lower()
    
    #logic for executing task based on query

        if "wikipedia" in query:
            speak("searching wikipedia...")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)
 
        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open google" in query:
            path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe %s "
            webbrowser.get(path).open("google.com")

        elif "stack overflow" in query:
            webbrowser.open("stackoverflow.com") 

        elif "play music" in query:
            music_dir="D:\\music\\favSongs"
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        
        elif "the time" in query:
            time=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is{time}")

        elif "open vs code" in query:
            codepath="C:\\Users\\shrey\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe"
            os.startfile(codepath)

        elif "email to yash" in query:
            try:
                speak("what should i say?")
                content=takeCommand()
                to= "receiver@gmail.com"
                sendEmail(to,content)
                speak("email has been sent")
            except Exception as e:
                print(e)
                speak("couldn't send email")
        
        elif "artificial intelligence" in query:
            ai(prompt=query)
            

        elif "quit" in query:
            quit()

        else:
            chat(query)
            