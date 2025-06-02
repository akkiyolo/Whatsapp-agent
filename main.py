# main.py
from rss_fetcher import fetch_news
from summarizer import summarize
from whatsapp_sender import send_whatsapp_message
from config import PHONE_NUMBER

def main():
    news_items = fetch_news()
    formatted_news = []

    for item in news_items:
        title = item.title
        description = item.summary
        link = item.link

        try:
            summary = summarize(title, description)
        except Exception as e:
            summary = title  # Fallback to title if summarization fails
            print(f"Error summarizing: {e}")

        formatted_news.append(f"📰 {summary}\n🔗 {link}\n")

    final_message = "\n\n".join(formatted_news)
    print("Sending the following news:\n", final_message)

    send_whatsapp_message(final_message, PHONE_NUMBER)

if __name__ == "__main__":
    main()
