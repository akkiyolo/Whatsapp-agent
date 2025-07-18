# 🛡️ Defense News WhatsApp Agent

This is an automated Python **agent** that fetches the latest **defense-related news**, summarizes it using the **Gemini AI API**, and sends it directly to your **WhatsApp number** — fully automatically.

## 📦 Features

- 🔍 Fetches real-time defense news via **Google News RSS**
- 🧠 Summarizes articles using **Gemini (Google Generative AI)**
- 📲 Sends messages to WhatsApp Web using **pywhatkit**
- 🤖 Auto-presses "Send" using **pyautogui** — no manual action required!
- ⚙️ Configurable number of articles, phone number, and kill switch

---

## 📁 Project Structure

defense_news_agent/
│
├── config.py # Contains settings like phone number and API key
├── main.py # Entry point: Fetches, summarizes, and sends the news
├── rss_fetcher.py # Gets latest defense news using RSS
├── summarizer.py # Summarizes content using Gemini API
├── requirements.txt # Python dependencies
└── README.md # Project guide #   W h a t s a p p - a g e n t  
 