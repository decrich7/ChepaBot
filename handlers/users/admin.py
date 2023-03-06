# -*- coding: utf-8 -*-
from aiogram.dispatcher import FSMContext
from aiogram import types
from random import randint
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher.filters import Command
from aiogram.types import InputFile, ReplyKeyboardRemove
from keyboards.default.type_tovar import type_menu
from keyboards.inline.menu_admin import crud_admin
from data.config import ADMINS
from aiogram.types import CallbackQuery
from states.add_tovar import Add
from keyboards.inline.menu import catalog
from loader import dp, bot



@dp.message_handler(Command("admin"))
async def admin(message: types.Message):
    if str(message.from_user.id) in ADMINS:
        num = randint(0, 1)
        await bot.send_photo(chat_id=message.from_user.id,
                             photo=InputFile(path_or_bytesio=f"img/admin{num}.jpg"),
                             caption="Здарова заебал 😎\n"
                                     "Ты находишся в админ панели бота, здесь ты можешь:\n"
                                     "1. Добавлять товары в различные категории\n"
                                     "2. Изменять цены, названия товаров\n"
                                     "3. Удалять товары", reply_markup=crud_admin)
    else:
        await message.answer(f"Вы не являетесь администратором!")


