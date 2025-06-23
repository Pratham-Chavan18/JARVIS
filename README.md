# 🧠 JARVIS: Your Personal Desktop Voice Assistant

![Jarvis Banner](https://ik.imagekit.io/rmlbayysp/jarvis_header.gif)

**JARVIS** (Just A Rather Very Intelligent System) is a Python-based voice assistant that performs various desktop tasks using natural language commands. Inspired by Tony Stark’s AI, it helps with searches, weather, time, launching sites, answering queries, and more — all hands-free!

---

## ✨ Features

- 🔍 **Search** anything on Google or Wikipedia
- 🎬 **Open** YouTube, Google, Gmail, Stack Overflow
- 🌦️ Get **real-time weather** updates
- 🧠 Ask **WolframAlpha** mathematical or factual questions
- 🕒 Know the **current time**
- 📰 Open **news** from Times of India
- 💬 Friendly interaction with **voice recognition & TTS**
- 🔐 Log off / Shut down your system via voice
- 📖 Help command to list features

![Features GIF](https://ik.imagekit.io/rmlbayysp/jarvis_features.gif)

---

## 🛠️ Prerequisites

Before running JARVIS, make sure you have the following installed:

| Requirement        | Install Command                                          |
|--------------------|----------------------------------------------------------|
| Python 3.x         | [Download Python](https://www.python.org/downloads/)     |
| `pyttsx3`          | `pip install pyttsx3`                                    |
| `SpeechRecognition`| `pip install SpeechRecognition`                          |
| `wikipedia`        | `pip install wikipedia`                                  |
| `wolframalpha`     | `pip install wolframalpha`                               |
| `requests`         | `pip install requests`                                   |
| `pyaudio`*         | `pip install pyaudio`                                    |
| `sapi5` engine     | Comes pre-installed with **Windows OS**                  |

---

🔐 API Keys
This assistant uses:

OpenWeatherMap API
Get your API key from: https://openweathermap.org/api
Replace it
api_key = "YOUR_API_KEY"

WolframAlpha App ID
Get it from: https://developer.wolframalpha.com/portal/myapps
Replace it

📌 Note
Works best on Windows due to sapi5 and pyaudio.
Avoid long pauses while speaking your command.
Keep internet connection active for search and weather tasks.

## 🧪 Setup

```bash
git clone
cd jarvis-ai-assistant
python jarvis.py
