import feedparser
import json
from datetime import datetime

# Список RSS-лент
rss_feeds = [
    "https://meduza.io/rss/all",
    "https://vc.ru/rss",
    "https://nplus1.ru/rss",
    "https://takiedela.ru/rss",
    "https://www.the-village.ru/rss",
    "https://habr.com/ru/rss/interesting/",
    "https://health.mail.ru/rss/",
    "https://indicator.ru/export/rss2/index.xml",
    "https://iz.ru/xml/rss/all.xml",
    "https://lenta.ru/rss/news"
]

# Ключевые слова
keywords = ["здоровье", "витамин", "красота", "питание", "фитнес", "медицина", "психолог"]

articles = []

for feed_url in rss_feeds:
    feed = feedparser.parse(feed_url)
    for entry in feed.entries:
        text = (entry.get("title", "") + " " + entry.get("summary", "")).lower()
        if any(kw in text for kw in keywords):
            articles.append({
                "title": entry.get("title", ""),
                "summary": entry.get("summary", ""),
                "link": entry.get("link", ""),
                "published": entry.get("published", "")
            })

# Сохраняем только 10 последних
articles = sorted(articles, key=lambda x: x["published"], reverse=True)[:10]

with open("articles.json", "w", encoding="utf-8") as f:
    json.dump(articles, f, ensure_ascii=False, indent=2)
