from aiogram import Router, types
from aiogram.filters import Command

from src.resources.messages import Messages
from src.keyboards.main_kb import show_main_menu_kb

commands_router = Router(name="commands")


@commands_router.message(Command('start'))
async def start(message: types.Message):
    await message.reply(
        Messages.start_message,
        reply_markup=show_main_menu_kb()
    )