from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from src.resources.messages import ButtonMessages

def submit_form_kb():
    kb = [
        [KeyboardButton(text=ButtonMessages.cancel_action)]
    ]

    return ReplyKeyboardMarkup(
        keyboard = kb,
        resize_keyboard=True,
        one_time_keyboard=True
    )