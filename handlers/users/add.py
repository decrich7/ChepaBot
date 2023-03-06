# -*- coding: utf-8 -*-
from aiogram.dispatcher import FSMContext
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher.filters import Command
from aiogram.types import InputFile, ReplyKeyboardRemove
from keyboards.default.type_tovar import type_menu
from keyboards.inline.menu_admin import crud_admin
from data.config import ADMINS
from aiogram.types import CallbackQuery
from states.add_tovar import Add
from keyboards.inline.menu import catalog
from loader import dp, bot, db


dict_type = {'📱 iPhone 📱': 'iphone', '💻 MacBook 💻': 'macbook', '📱 iPad 📱': 'ipad',
             '⌚️ Apple Watch ⌚️': 'apple watch', '🎧 AirPods 🎧': 'airpods',  '🔊 Музыкальные станции 🔊': 'music', '🎮 Игровые приставки 🎮': 'game'}


@dp.callback_query_handler(text_contains="add")
async def add(call: CallbackQuery):
    await call.answer(cache_time=5)
    await Add.type_tovar.set()
    if str(call.from_user.id) in ADMINS:
        await call.message.answer('⬇️Выбери тип товара который хочешь добавить ⬇️', reply_markup=type_menu)

@dp.message_handler(state=Add.type_tovar)
async def type_tovar_def(message: types.Message, state: FSMContext):
    type_tovar = message.text
    if type_tovar == '❌ Отмена ❌':
        await state.finish()
        await message.answer('Действие отменено, Чтобы перейти в меню админа, нажмите /admin',
                             reply_markup=ReplyKeyboardRemove())
    else:
        await state.update_data(type_tovar=dict_type[type_tovar])
        await message.answer("Введи название товара", reply_markup=ReplyKeyboardRemove())

        await Add.next()

@dp.message_handler(state=Add.name)
async def name_def(message: types.Message, state: FSMContext):
    name = message.text
    await state.update_data(name_tovar=name)
    await message.answer("Введи цену товара")

    await Add.next()


@dp.message_handler(state=Add.price)
async def price_def(message: types.Message, state: FSMContext):
    data = await state.get_data()
    price_tovar = message.text
    name_tovar = data.get("name_tovar")
    type_tovar = data.get('type_tovar')
    await db.add_tovar(type=type_tovar, name=name_tovar, price=price_tovar)
    await message.answer(f'Добавлен товар\n🔹 {name_tovar} - {price_tovar} <strong>₽</strong> 🔹')
    await state.finish()
