import pyaudio
import speech_recognition as sr  # this module should be installed with alias sr.
import datetime  # this is an inbuilt module in python, no need to do pip install in terminal.
import pyttsx3  # this is a module, meaning python text to speech.
import wikipedia  # this module should be installed using pip install.
import webbrowser  # this module is for opening youtube.
import os  # this module does all system related tasks.
import smtplib  # this module used to send gmail through programs.

"""After importing the library/module, we need to initialize using init().
Init function may take 2 arguments.
init(driverName string, debug bool)

drivername : [Name of available driver] sapi5 on Windows, nsss on MacOS.
debug: to enable or disable debug output"""

engine = pyttsx3.init("sapi5")  # initialization of the module in windows using "sapi5" driver.
voices = engine.getProperty("voices")  # In the "engine" object, we have "voices" attribute.
# print(voices)  # the attribute "voices" is a list and has 2 items, male and female voices at 2 locations.
# remember, these 2 voices are also objects at 2 locations.
# print(voices[0].id)  # note:- If we print "object.id" we get location of the object with few details.
# print(voices[1].id)  # HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0
engine.setProperty("voice", voices[0].id)  # voice is the property and value is set to male voice.


def speak(string):  # means the string will be spoken by the tts
    engine.say(string)
    engine.runAndWait()  # this function should be called, then only speak() works


def wishMe():  # this function wishes me on the basis of date and time.
    hour = int(datetime.datetime.now().hour)  # inside datetime module, datetime class, "now().hour" gives hour.
    if hour >= 0 and hour < 12:  # it means time in AM.
        speak("Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    speak("Hello sir, I am Jarvis, how can I help you??")


def takeCommand():  # this function takes audio in speaker as input and gives output as string.
    r = sr.Recognizer()  # Recognizer is the class which helps us to recognize the audio. Here "r" is the object.
    with sr.Microphone() as source:  # creates an instance of microphone in the computer.
        print("listening...")
        r.pause_threshold = 1  # if 1 second time is given while speaking, then phrase won't be completed.
        audio = r.listen(source)  # listens audio in the microphone.

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language="en-in")  # it is the output text file.
        print("User said: ", query)

    except Exception as e:
        # print(e)  # this statement should not be shown, user should only see below statement in case of error.
        print("Say that again please....")
        return "None"  # here None is simply a string, not the python value.

    return query  # text file given as output, we should get that in return.


def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("shiva.nanda366@gmail.com", "your-password")  # make a text file, bring here using file pointer.
    server.sendmail("shiva.nanda366@gmail.com", to, content)
    server.close()



if __name__ == '__main__':
    wishMe()

    while True:
        query_final = takeCommand().lower()  # everything will be in lower case.

        # we should write the logic for executing the tasks based on query.
        if "wikipedia" in query_final:
            speak("Searching wikipedia....")
            query_latest = query_final.replace("wikipedia", "")
            results = wikipedia.summary(query_latest, sentences=6)  # gives 6 sentences from the wikipedia.
            speak(results)
            print(f"According to wikipedia {results}")  # results will be spoken out using speak().


        elif "open youtube" in query_final:
            webbrowser.open("youtube.com")

        elif "open google" in query_final:
            webbrowser.open("google.com")

        elif "trading view" in query_final:
            webbrowser.open("www.tradingview.com")

        elif "play music" in query_final:  # backslash inside a string should be inserted as double backslash.
            music_directory = "E:\\Songs\\other songs,devotional songs"  # directory should be in a string.
            songs = os.listdir(music_directory)  # listdir function gives list of files in the directory.
            print(songs)
            os.startfile(os.path.join(music_directory, songs[13]))  # this function takes folder, file as input.

        elif "the time" in query_final:
            ask_time = datetime.datetime.now().strftime("%H:%M:%S")  # we need time in str format.
            speak(f"Sir, the time is {ask_time}")

        elif "open pycharm" in query_final:
            code_directory = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\JetBrains"
            os.startfile(code_directory)

        elif "email to Shiva" in query_final:
            try:  # in the case of error, program should not stop. Let it continue.
                speak("What should I say??")
                text_content = takeCommand()  # calling the function again.
                to = "shiva.sh366@gmail.com"
                sendEmail(to, text_content)
                speak("Email has been sent")

            except Exception as e:
                print(e)
                speak("sorry sir, I am unable to send the email")

        elif "quit" in query_final:
            exit()
