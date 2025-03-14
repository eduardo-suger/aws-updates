import feedparser
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

# Coletar as atualizações da AWS
rss_url = "https://aws.amazon.com/new/feed/"
feed = feedparser.parse(rss_url)

# Criar o conteúdo do e-mail
if not feed.entries:
    email_content = "⚠️ Nenhuma atualização encontrada no AWS Updates."
else:
    email_content = "<h2>🚀 Últimas atualizações da AWS:</h2>"
    for entry in feed.entries[:5]:
        email_content += f"<h3>{entry.title}</h3>"
        email_content += f"<p>{entry.summary}</p>"
        email_content += f'<p><a href="{entry.link}">🔗 Leia mais</a></p><hr>'

# Configuração do e-mail (usando variáveis de ambiente do GitHub Secrets)
email_user = os.getenv("EMAIL_USER")
email_pass = os.getenv("EMAIL_PASS")
email_to = "seuemail@gmail.com"  # Substitua pelo seu e-mail de destino

# Criar a mensagem de e-mail
msg = MIMEMultipart()
msg["From"] = email_user
msg["To"] = email_to
msg["Subject"] = "🚀 Atualizações da AWS"

msg.attach(MIMEText(email_content, "html"))

# Enviar o e-mail via SMTP (Gmail)
try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email_user, email_pass)
    server.sendmail(email_user, email_to, msg.as_string())
    server.quit()
    print("✅ E-mail enviado com sucesso!")
except Exception as e:
    print(f"❌ Erro ao enviar e-mail: {e}")
