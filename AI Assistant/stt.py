import speech_recognition as sr
import sounddevice as sd
import numpy as np
import wave

SAMPLE_RATE = 16000
DURATION = 10

recognizer = sr.Recognizer()


def record(seconds=DURATION):
    print("Speak something...")
    data = sd.rec(
        int(seconds * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype="int16"
    )
    sd.wait()

    volume = np.max(np.abs(data))
    print("Recording volume:", volume)
    if volume < 100:
        print("Warning: Microphone volume is too low!")

    with wave.open("test.wav", "wb") as file:
        file.setnchannels(1)
        file.setsampwidth(2)
        file.setframerate(SAMPLE_RATE)
        file.writeframes(data.tobytes())

    return sr.AudioData(data.tobytes(), SAMPLE_RATE, 2)


def speech():
    audio = record(DURATION)
    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio, language="en-US")
        print("Recognized:", text)
        return text
    except sr.UnknownValueError:
        print("Google could not understand the audio.")
        return ""
    except sr.RequestError as e:
        print("API error:", e)
        return ""


if __name__ == "__main__":
    print(speech())