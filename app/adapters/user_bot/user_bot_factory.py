from pyrogram import Client

from app.core import settings

def start_user_bot():
    with Client(name=settings.user_bot.login, api_id=settings.user_bot.api_id,
                api_hash=settings.user_bot.api_hash) as bot:
        bot.run()

if __name__ == '__main__':
    start_user_bot()