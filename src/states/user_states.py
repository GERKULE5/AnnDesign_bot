from aiogram.fsm.state import State, StatesGroup


class SubmitForm(StatesGroup):
    name = State()
    phone = State()
    description = State()       