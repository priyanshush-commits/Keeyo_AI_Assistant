import pyttsx3
import speech_recognition 






engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
print(voices[0])
engine.setProperty("rate",180)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    

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

if  __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from GreetMe import greetME
            greetME()

            while True:
                query = takeCommand().lower()
                if "Its Time To Sleep Keeyo" in query:
                    speak("Ok Sir, You can call me again whenever you want")
                    
                    break

                    elif "hello" in query:
                    speak("Hello sir, How Are You")
                
                elif "i am fine":
                    speak("That's great sir")

                elif "How are you" in query:
                    speak("perfect sir")

                elif "thank you" in query:
                    speak("welcome sir")

                elif "google" in query:
                    from

                
    
