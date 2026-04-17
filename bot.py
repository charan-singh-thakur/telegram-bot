import re
import requests

print("BOT STARTED")

bot_token = "8741386792:AAGpqxQdeuCf66AIAu74PgXW5J2IENlbwhw"

source_channel = -1002071984432
target_channel = -1002113648943

keywords = [
    "sridevi",
    "time",
    "madhur",
    "milan",
    "rajdhani",
    "kalyan",
    "main"
]

last_message_id = None

def get_updates():
    global last_message_id

    url = f"https://api.telegram.org/bot{bot_token}/getUpdates"
    response = requests.get(url).json()

    for update in response.get("result", []):
        message = update.get("channel_post")

        if message:
            msg_id = message["message_id"]

            if last_message_id == msg_id:
                continue

            last_message_id = msg_id

            chat_id = message["chat"]["id"]

            if chat_id != source_channel:
                continue

            text = message.get("text", "").lower()
            print("MESSAGE:", text)

            if any(word in text for word in keywords):

                match = re.search(r'\d{3}-\d{2}-\d{3}', text)

                if match:
                    result = match.group()

                    msg = f"""🔻FASTEST LIVE UPDATE🔻

SRIDEVI NIGHT

{result}

सबसे तेज़-सबसे पहले।।

Refresh

LIVE UPDATES FOLLOW:=👇
➖➖➖➖➖➖➖➖➖
@Matka_officials
➖➖➖➖➖➖➖➖➖
"""

                    requests.post(
                        f"https://api.telegram.org/bot{bot_token}/sendMessage",
                        data={"chat_id": target_channel, "text": msg}
                    )

while True:
    try:
        get_updates()
    except Exception as e:
        print("ERROR:", e)
