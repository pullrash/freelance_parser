import os
import requests

# Дані з секретів GitHub
API_TOKEN = os.getenv("API_TOKEN")
TELEGRAM_TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

# ID навичок (169 — це Python, ти можеш додати інші через кому)
URL = "https://freelancehunt.com/projects?skills=169&skills=180"
DB_FILE = "last_id.txt"

def send_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "HTML",
        "disable_web_page_preview": False
    }
    try:
        requests.post(url, data=data)
    except Exception as e:
        print(f"Помилка відправки в Telegram: {e}")

def get_last_id():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as f:
            content = f.read().strip()
            return int(content) if content.isdigit() else 0
    return 0

def save_id(p_id):
    with open(DB_FILE, "w") as f:
        f.write(str(p_id))

def check_freelance():
    if not API_TOKEN:
        print("Помилка: API_TOKEN не знайдено!")
        return

    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    
    response = requests.get(URL, headers=headers)
    
    if response.status_code == 200:
        projects = response.json().get("data", [])
        last_id = get_last_id()
        new_last_id = last_id

        # API віддає нові проєкти зверху, тому перевертаємо список для черговості
        for project in reversed(projects):
            p_id = int(project["id"])
            
            if p_id > last_id:
                attr = project["attributes"]
                name = attr["name"]
                link = project["links"]["self"]["web"]
                
                # Формуємо бюджет
                budget = "Договірна"
                if attr.get("budget"):
                    budget = f"{attr['budget']['amount']} {attr['budget']['currency']}"
                
                msg = (
                    f"<b>🚀 Нове замовлення!</b>\n\n"
                    f"📝 <b>Назва:</b> {name}\n"
                    f"💰 <b>Бюджет:</b> {budget}\n\n"
                    f"🔗 <a href='{link}'>Відкрити проєкт</a>"
                )
                
                send_telegram(msg)
                new_last_id = p_id
                print(f"Надіслано проєкт ID: {p_id}")

        save_id(new_last_id)
    else:
        print(f"Помилка API: {response.status_code}, {response.text}")

if __name__ == "__main__":
    check_freelance()
