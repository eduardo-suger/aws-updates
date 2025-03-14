import feedparser
import json

# URL do feed RSS da AWS
rss_url = "https://aws.amazon.com/new/feed/"
feed = feedparser.parse(rss_url)

# Criar estrutura de dados para salvar no JSON
updates = {
    "source": "AWS Updates",
    "url": rss_url,
    "updates": []
}

# Adicionar as 5 últimas atualizações ao JSON
for entry in feed.entries[:5]:
    updates["updates"].append({
        "title": entry.title,
        "summary": entry.summary,
        "link": entry.link,
        "published": entry.published
    })

# Criar ou atualizar o arquivo JSON
with open("updates.json", "w", encoding="utf-8") as file:
    json.dump(updates, file, indent=4, ensure_ascii=False)

print("✅ Arquivo `updates.json` atualizado com sucesso!")
