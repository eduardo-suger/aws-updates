import feedparser

rss_url = "https://aws.amazon.com/new/feed/"
feed = feedparser.parse(rss_url)

print("🚀 Últimas atualizações da AWS:\n")

for entry in feed.entries[:5]:
    print(f"🔹 {entry.title}")
    print(f"📄 {entry.summary}")
    print(f"🔗 {entry.link}\n")
