## David's Virt Assistant : Milky

# Imports:
import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import wikipedia
import pyaudio
import pywhatkit as kit

#print(sr.Microphone.list_microphone_names())

# Recognizing Speech:
def spokeCMD():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I'm Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)
        
        try:
            print("Attempting to Recognize...")
            query = r.recognize_google(audio, language="en-in" )
            print("The Query: ", query)
            
        except Exception as d:
            print(d)
            print()
            print("Sorry I didn't get that. Please repeat that.")
            return "None"
        return query

# Responding:
def response(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    
    engine.setProperty('voice', voices[1].id)
    engine.say(audio)
    
    engine.runAndWait()
    
# Commands for Milky

# Actually Processing the Command
def take_query():
    
    while (True):
        query = spokeCMD().lower()
        
        if "hello milky" in query or "hello" in query:
            response("Hello there! I am Milky, your virtual Compainion.")
            continue
        
        
        elif "school work" in query:
            response("Opening your school work tabs.")
            webbrowser.open("https://champlain.instructure.com/")
            webbrowser.open("https://github.com/dthomsen116")
            webbrowser.open("https://drive.google.com/drive/my-drive")
            webbrowser.open("https://mail.google.com")
            continue
        
        elif "stop" in query or "goodbye" in query:
            response("See-ya later alligator!")
            exit()
            
        elif "who is" in query or "what is" in query or "where is" in query or "why is" in query or "when is" in query:
            
            response("Checking the wikipedia ")
            query = query.replace("who is", "")
            query = query.replace("what is", "")
            query = query.replace("why is", "")
            query = query.replace("when is", "")
            query = query.replace("where is", "")

            result = wikipedia.summary(query, sentences=4)
            response("According to wikipedia: ")
            response(result)
            
        elif "date today" in query:
            date = datetime.date.today()
            
            response("today is ")
            response(date)
        
        elif "play" in query:  
        ## Function Here
            query = query.replace("play", "")
            kit.playonyt(query)
            continue
            
if __name__ == '__main__': 
    take_query()
