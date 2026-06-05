import pyttsx3
import math

speaker=pyttsx3.init()

def speak(text):
    speaker.say(text)
    speaker.runAndWait()

def entreie():
    speak("Enter the password ")
    s=input("Enter the password ")   

    if s=="9999":

        print("Welcome")
        speak("Welcome")

        print("Hlo user What \n Go you want to \n Go \n Your options are below \n Addition \n Maximum \n Minimum \n Multiplication ")
        speak("Hlo user What \n Go you want to \n Go \n Your options are below \n Addition \n Maximum \n Minimum \n Multiplication ")

        speak("Enter the Numbers ")
        n=list(map(int,input("Enter the Numbers ").split(",")))

        speak("For the Addition enter add\n For the Maximum Enter maxi \n For the minimum number enter mini \n for muliply enter mul  ")
        ent=input("For the Addition enter add\n For the Maximum Enter maxi \n For the minimum number enter mini \n for multiply enter mul  ").lower()
    
        if ent=="add":
            a=sum(n)
            print(f"The sum of the numbers are:- {a}")

        elif ent=="maxi":
            a=max(n) 
            print(f"The maximum Numbe Among them is :-{a}")

        elif ent=="mini":
             a=min(n)
             print(f"The Minimum Number Among them is :-{a}")

        elif ent=="mul":   
            a=math.prod(n)
            print(f"The multiplication of the elements of the list is :-{a}")

        else:
            print("Invalid Selection") 
            speak("Invalid Selection")    
    else :
        print ("You are not the user \n Go to hell")   
        speak("You are not the user \n Go to hell")
entreie()        