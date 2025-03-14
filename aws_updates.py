import feedparser

# URL do feed RSS do Azure Updates
rss_url = "https://azure.microsoft.com/en-us/updates/feed/"

print("📡 Conectando ao feed RSS do Azure...")

# Obtém as atualizações do Azure
feed = feedparser.parse(rss_url)

# Verifica se há atualizações
if not feed.entries:
    print("⚠️ Nenhuma atualização encontrada! Pode ser um problema no feed do Azure.")
else:
    print("🚀 Últimas atualizações do Azure Marketplace:\n")
    for entry in feed.entries[:5]:  # Exibe as 5 mais recentes
        print(f"🔹 {entry.title}")
        print(f"📄 {entry.summary}")
        print(f"🔗 {entry.link}\n")
