
import feedparser
import json
import os

RSS_FEEDS = [
    "https://fitomarket.ru/blogs/news.atom",
    "https://apteka.ru/blog/rss/",
]

OUTPUT_FILE = "articles.json"

def fetch_articles():
    articles = []
    for feed_url in RSS_FEEDS:
        feed = feedparser.parse(feed_url)
        for entry in feed.entries[:5]:
            articles.append({
                "title": entry.title,
                "link": entry.link,
                "date": entry.published if "published" in entry else "",
                "summary": entry.summary if "summary" in entry else "",
            })
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(articles, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    fetch_articles()
