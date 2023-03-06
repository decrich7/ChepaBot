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
from states.change_tovar import Change
from keyboards.inline.menu import catalog
from loader import dp, bot, db
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

dict_type = {'📱 iPhone 📱': 'iphone', '💻 MacBook 💻': 'macbook', '📱 iPad 📱': 'ipad',
             '⌚️ Apple Watch ⌚️': 'apple watch', '🎧 AirPods 🎧': 'airpods', '🔊 Музыкальные станции 🔊': 'music',
             '🎮 Игровые приставки 🎮': 'game'}


@dp.callback_query_handler(text_contains="change")
async def change_def(call: CallbackQuery):
    await call.answer(cache_time=5)
    await Change.tovar.set()
    if str(call.from_user.id) in ADMINS:
        await call.message.answer('⬇️Выбери тип товара который хочешь изменить ⬇️', reply_markup=type_menu)


@dp.message_handler(state=Change.tovar)
async def type_tovar_def(message: types.Message, state: FSMContext):
    type_tovar = message.text
    if type_tovar == '❌ Отмена ❌':
        await state.finish()
        await message.answer('Действие отменено, Чтобы перейти в меню админа, нажмите /admin', reply_markup=ReplyKeyboardRemove())
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
        await message.answer("Выбери товар", reply_markup=buy)
        await Change.next()


@dp.callback_query_handler(state=Change.type_change)
async def change_def(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=5)
    data = call.data
    if data == 'exit':
        await state.finish()
        await call.message.answer('Действие отменено, Чтобы перейти в меню админа, нажмите /admin')
    else:
        await state.update_data(tovar_id=data)
        await call.message.answer("Выбери тип изменения", reply_markup=change_tovar)
        await Change.next()


@dp.callback_query_handler(state=Change.final)
async def new_type_def(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=5)
    data = call.data.split('_')[-1]
    await state.update_data(type_change=data)
    await call.message.answer("Теперь введи новое значение", reply_markup=ReplyKeyboardRemove())
    await Change.next()


@dp.message_handler(state=Change.final1)
async def value_def(message: types.Message, state: FSMContext):
    data = await state.get_data()

    value = message.text
    type_change = data.get('type_change')
    tovar_id = int(data.get('tovar_id'))
    type_tovar = data.get('type_tovar')
    try:
        if type_change == 'name':
            await db.update_name(value, tovar_id)
            await message.answer(f"Наименование товара успешно изменено на {value}")
        elif type_change == 'price':
            await db.update_price(value, tovar_id)
            await message.answer(f"Цена товара успешно изменено на {value} ₽")
    except Exception as E:
        await message.answer(f"Похоже произошла ошибка при изменении товара - {E}")

    await state.finish()