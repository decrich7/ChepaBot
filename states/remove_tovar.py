from aiogram.dispatcher.filters.state import StatesGroup, State


class Remove(StatesGroup):
    type_tovar = State()
    tovar_id = State()

