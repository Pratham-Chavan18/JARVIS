import os
import time
import subprocess
import json
import wolframalpha
import requests
import webbrowser
import wikipedia
import datetime
import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty("voice", voices[0].id)

def speak(text):
    print("JARVIS:", text)
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=8)
        except sr.WaitTimeoutError:
            print("Timeout: No speech detected.")
            return ""

    try:
        print("Recognizing...")
        statement = r.recognize_google(audio, language='en-in')
        print(f"You said: {statement}")
    except sr.UnknownValueError:
        print("Could not understand audio.")
        return ""
    except sr.RequestError:
        print("Speech service unavailable.")
        return ""
    return statement

def wishMe():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning Mr. Pratham Chavan.")
    elif 12 <= hour <= 18:
        speak("Good afternoon Mr. Pratham Chavan.")
    else:
        speak("Good evening Mr. Pratham Chavan. It's already night, consider getting some rest.")

def showHelp():
    help_text = """
    I can perform the following tasks:
    - "Wikipedia [topic]"
    - "Open YouTube", "Open Google", "Open Gmail", "Open Stack Overflow"
    - "Search [query]"
    - "Weather" (I will ask your city)
    - "Time"
    - "News"
    - "Ask [any question]" (maths, science, etc.)
    - "Who are you" / "Who made you"
    - "Log off" / "Shut down"
    - "Goodbye" or "Stop" to exit
    """
    print(help_text)
    speak("Here are the things I can do for you.")
    speak(help_text)

if __name__ == '__main__':
    speak("Loading your personal assistant JARVIS.")
    wishMe()
    showHelp()

    while True:
        speak("How can I help you?")
        statement = takeCommand().lower()

        if statement == "":
            continue

        if "goodbye" in statement or "ok bye" in statement or "stop" in statement:
            speak("JARVIS shutting down. Goodbye!")
            break

        elif 'wikipedia' in statement:
            speak("Searching Wikipedia...")
            try:
                statement = statement.replace("wikipedia", "")
                results = wikipedia.summary(statement, sentences=2)
                speak("According to Wikipedia")
                speak(results)
            except:
                speak("Sorry, I couldn't find that on Wikipedia.")

        elif "open youtube" in statement:
            webbrowser.open("https://www.youtube.com")
            speak("YouTube is now open.")

        elif "open google" in statement:
            webbrowser.open("https://www.google.com")
            speak("Google is now open.")

        elif "open gmail" in statement:
            webbrowser.open("https://www.gmail.com")
            speak("Gmail is now open.")

        elif "open stack overflow" in statement:
            webbrowser.open("https://stackoverflow.com")
            speak("Stack Overflow is now open.")

        elif "search" in statement:
            query = statement.replace("search", "")
            webbrowser.open(f"https://www.google.com/search?q={query}")
            speak(f"Searching for {query}")

        elif "weather" in statement:
            api_key = "8ef61edcf1c576d65d836254e11ea420"  # Replace with your API key
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            speak("Which city's weather would you like to know?")
            city_name = takeCommand()
            if city_name:
                complete_url = f"{base_url}q={city_name}&appid={api_key}"
                try:
                    response = requests.get(complete_url)
                    x = response.json()
                    if x["cod"] != "404":
                        main = x["main"]
                        weather = x["weather"][0]
                        temp = main["temp"]
                        humidity = main["humidity"]
                        desc = weather["description"]
                        report = (f"Temperature: {temp}K\n"
                                  f"Humidity: {humidity}%\n"
                                  f"Condition: {desc}")
                        speak(report)
                    else:
                        speak("City not found.")
                except:
                    speak("Unable to fetch weather at the moment.")
            else:
                speak("No city name received.")

        elif "time" in statement:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {current_time}")

        elif "who are you" in statement or "what can you do" in statement:
            speak("I am JARVIS, version 1.0, your virtual assistant. I can perform tasks such as web browsing, searching, weather reporting, and more.")

        elif "who made you" in statement or "who created you" in statement:
            speak("I was built by Pratham Chavan.")

        elif "news" in statement:
            webbrowser.open("https://timesofindia.indiatimes.com/home/headlines")
            speak("Opening Times of India for latest headlines.")

        elif "ask" in statement:
            speak("What would you like to ask?")
            question = takeCommand()
            app_id = "TJ8QQA-K6RGQRR4L9"  # Replace with your WolframAlpha App ID
            client = wolframalpha.Client(app_id)
            try:
                res = client.query(question)
                answer = next(res.results).text
                speak(answer)
            except:
                speak("Sorry, I couldn't fetch an answer for that.")

        elif "log off" in statement or "shut down" in statement:
            speak("Your system will shut down in 10 seconds. Please close all applications.")
            subprocess.call(["shutdown", "/s", "/t", "10"])
            break
