import speech_recognition
import pyttsx3
import pywhatkit
import wikipedia

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again please...")  
        return "None"
    return query

query = takeCommand().lower()

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
print(voices[0])
engine.setProperty("rate",180)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def searchGoogle(query):
  if "google" in query:
    import wikipedia as googleScrap
    query = query.replace("keeyo","")
     query = query.replace("google search","")
     query = query.replace("google","")
     speak("This is what I found on google")

    try:
        pywhatkit.search(query)
        result = googleScrap.summary(query,1)
        speak(result)
      
    
    
