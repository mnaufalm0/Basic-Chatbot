import speech_recognition as sr
import pyttsx3
import datetime
import math
import wikipedia
# Basic-Chatbot
recognizer = sr.Recognizer()
tts = pyttsx3.init()

def speak(text):
    print(f"Bot: {text}")
    tts.say(text)
    tts.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Speak now...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
        return None
    except sr.RequestError as e:
        speak(f"Google Speech Recognition error: {e}")
        return None

def tell_time():
    now = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The current time is {now}")

def tell_date():
    today = datetime.datetime.now().strftime("%A, %d %B %Y")
    speak(f"Today is {today}")

def solve_math(expression):
    try:
        # Replace spoken words with operators
        expression = expression.replace("plus", "+").replace("minus", "-").replace("times", "*")
        expression = expression.replace("x", "*").replace("into", "*").replace("divide", "/")
        result = eval(expression)
        speak(f"The result is {result}")
    except:
        speak("Sorry, I couldn't solve that.")

def search_wikipedia(query):
    try:
        summary = wikipedia.summary(query, sentences=2)
        speak(f"According to Wikipedia, {summary}")
    except:
        speak("Sorry, I couldn't find information on that.")

def chatbot_reply(message):
    if message is None:
        return
    if "hello" in message or "hi" in message:
        speak("Hello! How can I assist you today?")
    elif "how are you" in message:
        speak("I'm fine. Thanks for asking!")
    elif "your name" in message:
        speak("I'm VoiceBot, your personal voice assistant.")
    elif "time" in message:
        tell_time()
    elif "date" in message:
        tell_date()
    elif "stop" in message or "exit" in message or "goodbye" in message:
        speak("Goodbye, have a wonderful day!")
        exit()
    elif "what is" in message or "calculate" in message:
        expression = message.replace("what is", "").replace("calculate", "")
        solve_math(expression)
    elif "who is" in message or "what is" in message:
        query = message.replace("who is", "").replace("what is", "")
        search_wikipedia(query)
    else:
        speak("Sorry, I don't understand that.")

# Main loop
while True:
    user_command = listen()
    if user_command:
        chatbot_reply(user_command)
