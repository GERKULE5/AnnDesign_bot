from aiogram import Router, types, F, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile, InputMediaPhoto, ReplyKeyboardMarkup, ReplyKeyboardRemove
from pathlib import Path

from src.database.dao import add_user
from src.resources.messages import ButtonMessages, ServicesMessages, ContactsMessages, SubmitFormMessages, Messages
from src.states.user_states import SubmitForm
from src.keyboards.submit_form_kb import submit_form_kb
from src.keyboards.main_kb import main_menu_kb
from src.utils.notifications import notify_admin



MAIN_DIR = Path(__file__).parent.parent.parent
IMAGE_DIR = MAIN_DIR / "src" / "resources" / "images"


texts_router = Router(name="texts")

# -------- Услуги --------
@texts_router.message(F.text == ButtonMessages.services_btn)
async def get_services(message: types.Message):
    await message.reply(
        f'1. {ServicesMessages.logo}\n2. {ServicesMessages.style}\n3. {ServicesMessages.illustrations}'
    )

# -------- Портфолио --------
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

# -------- Контакты --------
@texts_router.message(F.text == ButtonMessages.contacts_btn)
async def get_contacts(message: types.Message):
    await message.reply(
        ContactsMessages.contacts.format(
            username = "@anna_designer231", 
            email = "anna_design_logo@gmail.com")
    )
# -------- Оставить заявку --------
@texts_router.message(F.text == ButtonMessages.submit_button)
async def start_submit(message: types.Message, state: FSMContext):
  
    await message.reply(SubmitFormMessages.name_message, reply_markup=submit_form_kb())
    await state.set_state(SubmitForm.name)

@texts_router.message(F.text == ButtonMessages.cancel_action)
async def cancel_action(message: types.Message, state: FSMContext):
    current_state = await state.get_state()

    if current_state is None:
        return
    await state.clear()
    await message.answer(
        SubmitFormMessages.cancel_message,
        reply_markup= main_menu_kb()
    )                  

@texts_router.message(SubmitForm.name)
async def process_name(message: types.Message, state: FSMContext):
    if not message.text or not message.text.strip():
        await message.reply(SubmitFormMessages.incorrect_name)
        return
    
    await state.update_data(name=message.text.strip())
    await message.reply(SubmitFormMessages.phone_message)
    await state.set_state(SubmitForm.phone)

@texts_router.message(SubmitForm.phone)
async def process_phone(message: types.Message, state: FSMContext):
    if not message.text:
        await message.reply(SubmitFormMessages.incorrect_phone)
        return                                                                  

    await state.update_data(phone=message.text)
    await message.reply(SubmitFormMessages.description_message) 
    await state.set_state(SubmitForm.description)

@texts_router.message(SubmitForm.description)
async def process_description(message: types.Message, state: FSMContext, bot: Bot):
    if not message.text:
        await message.reply(SubmitFormMessages.incorect_description)                                                                                        
        return

    await state.update_data(description=message.text)
    data = await state.get_data()
    add_user(
        user_id=message.from_user.id,
        username=message.from_user.username,
        name=data['name'],
        phone=data['phone'],
        description=data['description']
    )
    print(data)
    await message.reply(SubmitFormMessages.final_message, reply_markup=main_menu_kb())
    await state.clear()
    await notify_admin(bot,data, user_id=message.from_user.id, username=message.from_user.username)
# Должен быть последним, иначе перехватит всё
@texts_router.message()
async def fallback_handler(message: types.Message):
    await message.answer(
        Messages.start_message,
        reply_markup=main_menu_kb()
    )                                                        