import os
import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from dotenv import load_dotenv

from src.handlers.commands import commands_router
from src.handlers.texts import texts_router
from src.database.db import init_db


load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

dp = Dispatcher()

dp.include_router(commands_router)
dp.include_router(texts_router)


async def main():

    bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    init_db()
    asyncio.run(main())                                                                         