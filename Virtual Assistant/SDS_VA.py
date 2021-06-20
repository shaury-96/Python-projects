import pyttsx3 as pt
import speech_recognition as sr
import webbrowser
import wikipedia
import datetime
import time
import os
import random


engine=pt.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)


def speak(aud):
    engine.say(aud)
    engine.runAndWait()


def logs(l):
    with open(f"logs.txt", "a") as op:
        op.write(str([str(datetime.datetime.now())]) + " : " + l + "\n")

def ts():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening....")
        r.pause_threshold = 1
        r.energy_threshold = 500
        audio = r.listen(source)
    try:
        speak("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        print(f"Sir ordered:{query}\n")
    except Exception as e:
        print(e)
        speak("Say that again sir...")
        return "None"
    return query



def sds():
    eid=str(input("Enter your email id to activate your virtual assistant:"))

    if "@" in eid:

        print("Activated")
        print("Start with a hello/hi/hey!!!")
        logs(f"Email id entered:{eid}")


        while True:


            query=ts()
            x=query.lower().split(' ')

            greetings = ["hello", "hi", "hey"]
            wish = {"morning": "Good morning", "night": "Good night", "care": "You too.", "bye": "Please don't go"}
            silly = {"married": "No, but i have a girlfriend", "love": "I love myself Sir", "hate": "lmao, look at your face ",
                     "children": "Oh please."}
            for word in x:
                if word in greetings:
                    h = int(datetime.datetime.now().hour)

                    if h >= 0 and h <= 12:
                        speak("Good Morning my majesty")
                    elif h > 12 and h <= 5:
                        speak("Good afternoon boss")
                    else:
                        speak("Good evening Sir")
                    speak("I am your virtual Assistant SDS, how may I help you?")
                    logs(query)
                    break

                elif word in wish:
                    answer = wish[word]
                    speak(answer)
                    logs(query)
                    break

                elif "time" in x:
                    a = str(datetime.datetime.now())
                    b = a[10:19].split(":")
                    d = f"Time is {b[0]}hour {b[1]}minutes {b[0]}seconds"
                    print(d)
                    speak(d)
                    logs(query)
                    break

                elif "date" in x:
                    a = str(datetime.datetime.now())
                    b = a[0:10].split("-")
                    c = {"1": "January", "2": "February", "3": "March", "4": "April", "5": "May", "6": "June", "7": "July",
                         "8": "August", "9": "September", "10": "October", "11": "November", "12": "December"}
                    b[1] = c[b[1]]
                    d = f"Date is {b[2]} {b[1]} {b[0]}"
                    print(d)
                    speak(d)
                    logs(query)
                    break

                elif "play vedio" in x:
                    webbrowser.open(f"https://www.youtube.com/results?search_query={x[1:]}")
                    logs(query)
                    break

                elif "search" in x:
                    webbrowser.open(f"https://www.google.com/results?search_query={x[1:]}")
                    logs(query)
                    break

                elif "what" in x or "who" in x:

                    try:
                        query = query.replace("who", "")

                    except:
                        query = query.replace("what", "")
                    answer = wikipedia.summary(query, sentences=2)
                    print(answer)
                    speak(answer)
                    logs(query)
                    break


                elif word in silly:
                    answer = silly[word]
                    speak(answer)
                    logs(query)
                    break

                elif "encrypt" and "pdf" in x:
                    speak("just type the location of file in this format")
                    print("A:\\...\\...")
                    f=str(input("Type here:"))
                    gp=str(input("Type the general password:"))
                    op=str(input("Type the owner password:"))
                    print(f"General password:{gp}")
                    print(f"Owner password:{op}")
                    from PyPDF2 import PdfFileWriter, PdfFileReader
                    pdfl = [f+".pdf"]
                    obj = PdfFileWriter()

                    for i in pdfl:
                        x = PdfFileReader(i)
                        pages = x.getNumPages()

                        for j in range(pages):
                            p = x.getPage(j)
                            obj.addPage(p)

                    a = open(f+"encrypt.pdf", "wb")
                    obj.encrypt(gp,op,True)
                    obj.write(a)
                    a.close()
                    print(f"File encrypted successfully at same location with name {f}encrypt")
                    speak("File encrypted successfully")
                    logs(query)
                    break






                elif "open" and "notepad" in x:

                    speak("Enter file name without extension")
                    q=str(input("Type here:"))
                    speak("Start seaking the content after saying Listening....")
                    note=ts()
                    print(note)
                    with open(f"{q}+.txt", "a") as op:
                        op.write(note)
                        print("successfully written")
                    logs(query)
                    break

                elif "open" and "word" in x:
                    speak("Enter file name without extension")
                    q = str(input("Type here:"))
                    speak("Start seaking the content after saying Listening....")
                    note = ts()
                    print(note)
                    with open(f"{q}+.docx", "a") as op:
                        op.write(note)
                        print("successfully written")
                    logs(query)
                    break


                elif "class" and "attend" in x:

                    b=webbrowser.open("https://meet.google.com/")
                    logs(query)
                    break

                elif 'play music' in x:
                    mdir = 'F:\\SONGS\\english'
                    songs = os.listdir(mdir)
                    os.startfile(os.path.join(mdir, songs[random.randint(0,186)]))
                    logs(query)
                    break


                elif "exit" in x:
                    speak("Thank You Sir")
                    speak("Meet you again soon")
                    logs(query)
                    print("Exiting....")
                    time.sleep(3)
                    exit()




    else:
        print("You have entered wrong email id")
        print("Access denied!!")
        print("Enter id again")
        sds()

sds()

