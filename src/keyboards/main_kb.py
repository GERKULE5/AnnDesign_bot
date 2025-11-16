from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from src.resources.messages import ButtonMessages

def main_menu_kb():
    kb = [
        [KeyboardButton(text=ButtonMessages.services_btn)], [KeyboardButton(text=ButtonMessages.portfolio_btn)],
        [KeyboardButton(text=ButtonMessages.contacts_btn)], [KeyboardButton(text=ButtonMessages.submit_button)]
    ]

    return ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        one_time_keyboard=False
    )