# whatsapp_sender.py
import pywhatkit as kit
import datetime

def send_whatsapp_message(message, phone):
    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute + 2  # Give some buffer to open WhatsApp Web

    kit.sendwhatmsg(phone, message, hour, minute)
