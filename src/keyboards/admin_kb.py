from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

from src.resources.messages import AdminNotifyMessages

def answer_to_application(user_id: int, username: str | None):
    if username:
        url = f"https://t.me/{username}"
    else:
        url = f"tg://user?id={user_id}"

    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=AdminNotifyMessages.type_to_user, url=url)]
        ]
    )
    return markup
