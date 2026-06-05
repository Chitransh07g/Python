import pyttsx3

engine = pyttsx3.init()

# Set speech rate
engine.setProperty('rate', 150)

# Get available voices
voices = engine.getProperty('voices')

# Set voice: usually voices[0] = male, voices[1] = female (depends on OS)
engine.setProperty('voice', voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def getinput():
    name = input("Enter your Name: ")
    roll = int(input("Enter your Roll Number: "))

    message = f"As per your input, your name is {name}.\nAs per your input, your Roll Number is: {roll}."
    speak(message)
    print(message)

getinput()
