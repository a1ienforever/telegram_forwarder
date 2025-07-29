import asyncio
import logging

from app.interfaces.bot import start_bot

if __name__ == "__main__":
    try:
        asyncio.run(start_bot())
    except (KeyboardInterrupt, SystemExit):
        logging.error("Бот был выключен!")