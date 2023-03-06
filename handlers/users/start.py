# -*- coding: utf-8 -*-

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.inline.menu import catalog
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    print(message.from_user)
    await message.answer(f"Привет, {message.from_user.full_name}! 👋\n"
                         f"Здесь ты можешь посмотреть актуальные цены и наличие товаров", reply_markup=catalog)


