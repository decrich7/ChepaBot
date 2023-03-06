from aiogram.dispatcher.filters.state import StatesGroup, State


class Add(StatesGroup):
    type_tovar = State()
    name = State()
    price = State()
