from aiogram import Router, types, F

from aiogram.types import FSInputFile, InputMediaPhoto
from pathlib import Path

from src.resources.messages import ButtonMessages, ServicesMessages, ContactsMessages


MAIN_DIR = Path(__file__).parent.parent.parent
IMAGE_DIR = MAIN_DIR / "src" / "resources" / "images"


texts_router = Router(name="texts")


@texts_router.message(F.text == ButtonMessages.services_btn)
async def get_services(message: types.Message):
    await message.reply(
        f'1. {ServicesMessages.logo}\n2. {ServicesMessages.style}\n3. {ServicesMessages.illustrations}'
    )


@texts_router.message(F.text == ButtonMessages.portfolio_btn)
async def get_portfolio(message: types.Message):
    images_paths = {'Логотип для кофейни "Bean There"': 'bean_there_logo.webp', 
                    'Логотип для центра ремонта мобильных телефонов': 'mobile_repare_logo.webp', 
                    'Логотип для домашней кондитерской': 'sweet_cake_logo.webp'}
    media_group = []
    for caption, file_name in images_paths.items():
        images_path = IMAGE_DIR / file_name

        if not images_path.exists():
            continue

        photo = FSInputFile(images_path)
        media_group.append(InputMediaPhoto(media=photo, caption=caption))
    if media_group:
        await message.answer_media_group(media=media_group)


@texts_router.message(F.text == ButtonMessages.contacts_btn)
async def get_contacts(message: types.Message):
    await message.reply(
        ContactsMessages.contacts.format(
            username = "@anna_designer231", 
            email = "anna_design_logo@gmail.com")
    )