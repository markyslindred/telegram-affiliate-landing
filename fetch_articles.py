
import feedparser
import json
from datetime import datetime

RSS_URL = "https://meduza.io/rss2/all"
OUTPUT = "articles.json"

def fetch_articles():
    feed = feedparser.parse(RSS_URL)
    articles = []
    for entry in feed.entries[:5]:
        articles.append({
            "title": entry.title,
            "link": entry.link,
            "summary": entry.summary,
            "published": entry.published
        })
    with open(OUTPUT, "w", encoding="utf-8") as f:
        json.dump(articles, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    fetch_articles()
