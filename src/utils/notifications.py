import os
from aiogram import Bot
from dotenv import load_dotenv


from src.resources.messages import AdminNotifyMessages
from src.keyboards.admin_kb import answer_to_application
load_dotenv()

async def notify_admin(bot: Bot, data: dict, user_id: int, username: str | None):
    text = (
        AdminNotifyMessages.application.format(
            name = data['name'],
            phone = data['phone'],
            description = data['description']
        )
    )

    await bot.send_message(os.getenv("ADMIN_ID"), text, reply_markup=answer_to_application(user_id, username))