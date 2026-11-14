# AI-Assistant
# AI Assistant

A simple voice-controlled desktop assistant built with Python and Tkinter. Click a button, speak a command, and the assistant replies in text and speech.

## Features

- Voice input using your microphone (Google Speech Recognition)
- Spoken replies using offline text-to-speech (pyttsx3)
- Tkinter GUI with a chat log
- Current weather using the free Open-Meteo API (no API key needed)
- Opens websites such as YouTube, Google and Gaana
- Tells the current time

## Supported Commands

| Say something like...        | What happens                          |
| ---------------------------- | ------------------------------------- |
| "What is your name"          | Assistant introduces itself           |
| "Hello" / "Hey"              | Greets you back                       |
| "Good morning"               | Greets you back                       |
| "Time"                       | Tells the current time                |
| "Weather"                    | Reads out the current weather         |
| "Play music"                 | Opens gaana.com in your browser       |
| "YouTube"                    | Opens youtube.com                     |
| "Google"                     | Opens google.com                      |
| "Shutdown"                   | Replies "ok sir" and closes the app   |

## Project Structure

```
AI Assistant/
├── gui.py             # Tkinter window and buttons (run this file)
├── action.py          # Matches commands and decides the reply
├── stt.py             # Speech-to-text (records mic, sends to Google)
├── texttospeech.py    # Text-to-speech using pyttsx3
├── weather.py         # Fetches weather from Open-Meteo
└── image/
    └── chatbotai.jpg  # Image shown in the GUI
```

## Requirements

- Python 3.9 or newer
- A working microphone
- An internet connection (needed for speech recognition and weather)

Python packages:

- `SpeechRecognition`
- `sounddevice`
- `numpy`
- `pyttsx3`
- `requests`
- `Pillow`

Tkinter and `wave` come with Python.

## Installation

```bash
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>
pip install SpeechRecognition sounddevice numpy pyttsx3 requests Pillow
```

## Usage

Run the app from the project folder (the image path is relative):

```bash
python gui.py
```

1. Click **ASK**.
2. When the console prints `Speak something...`, say a command.
3. The chat log shows what you said and the assistant's reply, and the reply is also spoken aloud.

You can test each module on its own:

```bash
python stt.py       # records and prints what you said
python weather.py   # prints the weather sentence
```

## Configuration

- **Location:** change the latitude, longitude and city name in `weather.py` (the default is Patna, India).
- **Recording length:** change `DURATION` in `stt.py` (default is 10 seconds).
- **Language:** change `language="en-US"` in `stt.py` (for example `en-IN` for Indian English).
- **Speech speed:** change the rate offset in `texttospeech.py`.
- **Microphone:** if the wrong input device is used, set `sd.default.device = (index, None)` in `stt.py`. List devices with `sounddevice.query_devices()`.

## Troubleshooting

- **"Google could not understand the audio":** the recording is saved as `test.wav`. Play it to check that your voice was captured. Speak right after `Speak something...` appears and use a full sentence.
- **`No module named ...`:** make sure all `.py` files are in the same folder and that the package is installed with `pip`.
- **GUI freezes while listening:** recording currently blocks the window for the full duration.

## Roadmap

- Run recording and speaking in a separate thread so the GUI never freezes
- Make the SEND and DELETE buttons work (typed commands, clear chat)
- Add more commands (search, jokes, news, open apps)
- Stricter command matching

## Contributing

Pull requests and suggestions are welcome. Open an issue to discuss what you would like to change.

## License

This project is licensed under the MIT License. Add a `LICENSE` file to your repository to apply it.
