import speech_recognition as aa
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = aa.Recognizer()
machine = pyttsx3.init()

def talk(text):
    machine.say(text)
    machine.runAndWait()

def input_instruction():
    instruction = ""
    try:
        with aa.Microphone() as origin:
            print("listening...")
            speech = listener.listen(origin)
            instruction = listener.recognize_google(speech)
            instruction = instruction.lower()
            if 'jarvis' in instruction:
                print(instruction)
    except aa.UnknownValueError:
        print("Sorry, I did not understand that.")
    except aa.RequestError:
        print("Could not request results; check your network connection.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return instruction

def play_bro():
    instruction = input_instruction()
    print(instruction)
    if 'play' in instruction:
        song = instruction.replace('play', "").strip()
        talk(f"playing {song}")
        pywhatkit.playonyt(song)
    elif 'time'in instruction:
        
        time=datetime.datetime.now().strftime('%I:%M%p')
        talk(f"current time is {time}")
    elif 'how are you' in instruction:
        talk('iam  good how about you')
        
    elif 'what is your full name'in instruction:
        talk('thanks for asking bro actually my complete name is jarvis lucky')
    elif 'who is the 'in instruction:
        human=instruction.replace('who is the '," ")
        info=wikipedia.summary(human,5)
        print(info)
        talk(info)
        

play_bro()
