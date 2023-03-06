from aiogram.dispatcher.filters.state import StatesGroup, State


class Change(StatesGroup):
    type_tovar = State()
    tovar = State()
    type_change = State()
    final = State()
    final1 = State()
