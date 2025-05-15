import speech_recognition as sr

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You said:", text)
    except:
        print("Sorry, I could not understand.")
        
if __name__ == "__main__":
    listen()
