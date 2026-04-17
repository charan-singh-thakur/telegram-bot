from telethon import TelegramClient, events
import re
import requests

print("BOT STARTED")

api_id = 31617683
api_hash = "1abcdb1e9787e95d194052dc56eada05"
bot_token = "8741386792:AAGpqxQdeuCf66AIAu74PgXW5J2IENlbwhw"

source_channel = -1002071984432
target_channel = -1002113648943

client = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

keywords = [
    "sridevi",
    "time",
    "madhur",
    "milan",
    "rajdhani",
    "kalyan",
    "main"
]

@client.on(events.NewMessage(chats=source_channel))
async def handler(event):
    text = event.message.text.lower()
    print("MESSAGE:", text)

    if any(word in text for word in keywords):

        match = re.search(r'\d{3}-\d{2}-\d{3}|\d{3}-\d', text)

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

client.run_until_disconnected()
