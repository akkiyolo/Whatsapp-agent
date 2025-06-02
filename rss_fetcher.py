# rss_fetcher.py
import feedparser
from config import RSS_FEED_URL

def fetch_news(limit=5):
    feed = feedparser.parse(RSS_FEED_URL)
    return feed.entries[:limit]
