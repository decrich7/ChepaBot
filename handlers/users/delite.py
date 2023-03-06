# -*- coding: utf-8 -*-
from aiogram.dispatcher import FSMContext
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher.filters import Command
from aiogram.types import InputFile, ReplyKeyboardRemove
from keyboards.default.type_tovar import type_menu
from keyboards.inline.menu_admin import crud_admin, change_tovar
from data.config import ADMINS
from aiogram.types import CallbackQuery
from states.remove_tovar import Remove
from keyboards.inline.menu import catalog
from loader import dp, bot, db
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

dict_type = {'📱 iPhone 📱': 'iphone', '💻 MacBook 💻': 'macbook', '📱 iPad 📱': 'ipad',
             '⌚️ Apple Watch ⌚️': 'apple watch', '🎧 AirPods 🎧': 'airpods', '🔊 Музыкальные станции 🔊': 'music',
             '🎮 Игровые приставки 🎮': 'game'}


@dp.callback_query_handler(text_contains="remove")
async def change_def(call: CallbackQuery):
    await call.answer(cache_time=5)
    await Remove.type_tovar.set()
    if str(call.from_user.id) in ADMINS:
        await call.message.answer('⬇️Выбери тип товара который хочешь удалить ⬇️', reply_markup=type_menu)


@dp.message_handler(state=Remove.type_tovar)
async def type_tovar_def12(message: types.Message, state: FSMContext):
    type_tovar = message.text
    if type_tovar == '❌ Отмена ❌':
        await state.finish()
        await message.answer('Действие отменено, Чтобы перейти в меню админа, нажмите /admin',
                             reply_markup=ReplyKeyboardRemove())
    else:
        await state.update_data(type_tovar=dict_type[type_tovar])
        data = await db.select_product(type=dict_type[type_tovar])
        matrix = [data[i:i + 3] for i in range(0, len(data), 3)]
        markup = []
        for i in matrix:
            list_str = []
            for j in i:
                list_str.append(InlineKeyboardButton(text=j['name'], callback_data=j['id']))
            markup.append(list_str)
        markup.append([InlineKeyboardButton(text='Отмена', callback_data='exit')])

        buy = InlineKeyboardMarkup(inline_keyboard=markup)
        await message.answer("Выбери товар который хочешь удалить", reply_markup=buy)

        await Remove.next()


@dp.callback_query_handler(state=Remove.tovar_id)
async def delite_def(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=5)
    data = await state.get_data()
    if call.data == 'exit':
        await state.finish()
        await call.message.answer('Действие отменено, Чтобы перейти в меню админа, нажмите /admin',
                                  reply_markup=ReplyKeyboardRemove())
    else:
        type_tovar = data.get('type_tovar')
        try:
            await db.delite_tovar(int(call.data))
            await call.message.answer('Товар успешно удален')
        except Exception as E:
            await call.message.answer(f"Похоже произошла ошибка при изменении товара - {E}")

        # await call.message.answer("Выбери тип изменения", reply_markup=change_tovar)
        await state.finish()
