from telethon import TelegramClient, events
import re
import requests

print("BOT STARTED")

api_id = 31617683
api_hash = "1abcdb1e9787e95d194052dc56eada05"
bot_token = "8741386792:AAGpqxQdeuCf66AIAu74PgXW5J2IENIbwhw"

source_channel = -1002071984432
target_channel = -1002113648943

client = TelegramClient('session', api_id, api_hash)

keywords = [
    "sridevi",
    "time",
    "madhur",
    "milan",
    "rajdhani",
    "kalyan",
    "main"
]

@client.on(events.NewMessage)
async def handler(event):

    chat_id = event.chat_id
    text = event.message.text

    print("CHAT ID:", chat_id)
    print("MESSAGE:", text)

    if chat_id != source_channel:
        return

    if not text:
        return

    text_lower = text.lower()

    if not any(word in text_lower for word in keywords):
        return

    # 🔥 NEW: support "=" format (178=68=378)
    equal_match = re.search(r'\b\d{3}=\d{2}=\d{3}\b', text)

    # 🔥 dash format (156-21-579)
    dash_full = re.search(r'\b\d{3}-\d{2}-\d{3}\b', text)

    # 🔥 open format (156-2)
    dash_open = re.search(r'\b\d{3}-\d{1}\b', text)

    if equal_match:
        result = equal_match.group(0).replace("=", "-")  # convert to dash
    elif dash_full:
        result = dash_full.group(0)
    elif dash_open:
        result = dash_open.group(0)
    else:
        return

    # 🔥 game detect
    game = "RESULT"
    for word in keywords:
        if word in text_lower:
            game = word.upper()
            break

    msg = f"""🔻FASTEST LIVE UPDATE🔻

{game} NIGHT

{result}

सबसे तेज़-सबसे पहले।।

Refresh

LIVE UPDATES FOLLOW:=👇
➖➖➖➖➖➖➖➖➖
@Matka_officials 
➖➖➖➖➖➖➖➖➖"""

    requests.post(
        f"https://api.telegram.org/bot{bot_token}/sendMessage",
        data={"chat_id": target_channel, "text": msg},
        timeout=5
    )

client.start()
client.run_until_disconnected()
