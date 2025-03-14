import json

# Nome dos arquivos
json_file = "updates.json"
md_file = "updates.md"

# Carregar os dados do JSON
try:
    with open(json_file, "r", encoding="utf-8") as file:
        data = json.load(file)
except FileNotFoundError:
    print(f"❌ Erro: O arquivo {json_file} não foi encontrado.")
    exit(1)

# Criar o conteúdo do Markdown
md_content = "# 🚀 Atualizações da AWS\n\n"

if "updates" in data and data["updates"]:
    for update in data["updates"]:
        md_content += f"## 📌 {update['title']}\n"
        md_content += f"📄 {update['summary']}\n"
        md_content += f"[🔗 Leia mais]({update['link']})\n\n"
else:
    md_content += "⚠️ Nenhuma atualização disponível no momento.\n"

# Escrever no arquivo Markdown
with open(md_file, "w", encoding="utf-8") as file:
    file.write(md_content)

print("✅ Arquivo `updates.md` gerado com sucesso!")
