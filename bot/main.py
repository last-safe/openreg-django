from aiogram import Bot, Dispatcher
from django.conf import settings
import django

from pathlib import Path
import asyncio
import sys
import os


BASE_DIR = Path(__file__).resolve().parent

sys.path = [*map({BASE_DIR.__str__(): BASE_DIR.parent.__str__()}.get, sys.path, sys.path)]
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "OpenReg.settings")
django.setup()


from bot.app.handlers import *


bot = Bot(token=settings.TELEGRAM_TOKEN, parse_mode="html")
dp = Dispatcher()


async def main() -> None:
    dp.include_router(router)
    await bot.delete_webhook(True)

    logger.info("bot is running")
    await dp.start_polling(bot)


if (__name__ == "__main__"):
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        ...