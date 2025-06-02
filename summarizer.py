# summarizer.py
import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-pro")

def summarize(title, description):
    prompt = f"""
Summarize the following defense-related news in 1-2 lines for a WhatsApp channel. Keep it short, clear, and relevant.

Title: {title}
Description: {description}
"""
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        print(f"[Gemini Error] {e}")
        return title  # fallback

