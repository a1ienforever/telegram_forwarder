from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from app.core import settings, setup_logging
from app.adapters.redis import get_storage


async def start_bot():
    setup_logging()
    load_dotenv()
    storage = get_storage(settings)

    bot = Bot(token=settings.telegram.token)
    dp = Dispatcher(storage=storage)

    from app.adapters.bot.handlers import router_list
    dp.include_routers(*router_list)
    await dp.start_polling(bot)

