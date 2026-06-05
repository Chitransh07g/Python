import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 150)

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