import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def get_user_input():
    user_input = input("Enter the secret code: ")
    
    if user_input != "9999":
        print("Not the user")
        speak( " " )
        speak("   Alert! Alert ! Invalid input. You are not the user.")
    else:
        print("Access granted. Welcome!")
        speak("Access granted. Welcome!")

get_user_input()