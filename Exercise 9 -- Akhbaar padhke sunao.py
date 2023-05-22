# API KEY -- 30f0cadd38544a409356aa2a6a6a5e55

import requests
import json

def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.speak(str)

if __name__ == '__main__':
    speak("News for today are ")
    url=("https://newsapi.org/v2/top-headlines?country=in&apiKey=30f0cadd38544a409356aa2a6a6a5e55")
    news=requests.get(url).text
    news_dict=json.loads(news)
    arts = news_dict['articles']
    for article in arts:
        speak(article['title'])
        speak("Moving on to next news ")

speak("Thanks for listening")

import pyttsx3
engine = pyttsx3.init()
# engine.say("Helo Sahil , How are you ")
engine.runAndWait()