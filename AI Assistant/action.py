import datetime
import webbrowser
import texttospeech
import weather

def reply(msg):
    texttospeech.text_to_speech(msg)
    return msg

def Action(data):
    user_data = (data or "").lower()

    if not user_data:
        return reply("I didn't catch that")

    if "what is your name" in user_data:
        return reply("My name is Virtual Assistant")

    elif "hello" in user_data or "hey" in user_data or "hye" in user_data:
        return reply("Hey sir, how can I help you")

    elif "good morning" in user_data:
        return reply("Good morning sir")

    elif "time" in user_data:
        now = datetime.datetime.now().strftime("%I:%M %p")
        return reply(f"The time is {now}")

    elif "shutdown" in user_data:
        return reply("ok sir")

    elif "play music" in user_data:
        webbrowser.open("https://gaana.com/")
        return reply("gaana.com is ready for you")

    elif "youtube" in user_data:
        webbrowser.open("https://youtube.com/")
        return reply("YouTube is ready for you")

    elif "google" in user_data:
        webbrowser.open("https://google.com/")
        return reply("Google is ready for you")

    elif "weather" in user_data:
        return reply(weather.get_weather())

    else:
        return reply("I'm not able to understand")