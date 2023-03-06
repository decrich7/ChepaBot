# -*- coding: utf-8 -*-

import logging
from aiogram.types import InputFile

from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery

from keyboards.inline.menu import buy
from loader import dp, bot, db


@dp.callback_query_handler(text_contains="tovar")
async def items(call: CallbackQuery):
    await call.answer(cache_time=10)
    list_item = [' ✅ <strong>Устройста в наличии</strong> ✅ ']
    type_tovar = call.data.split('_')[-1]
    dict_img = {'iphone': 'img/YgWXwhEuZkU.jpg', 'apple watch': 'img/eT-uWbVvkCQ.jpg', 'airpods': 'img/72fRjhTc3AY.jpg',
                'ipad': 'img/5facHpyRkEA.jpg', 'macbook': 'img/2BhtJfCaMIE.jpg', 'game': 'img/45NzvUgBv-E.jpg',
                'music': 'img/колонки.jpg'}
    data = await db.select_product(type=type_tovar)
    for i in data:
        list_item.append(f'🔹 {i["name"]} - {i["price"]} <strong>₽</strong> 🔹')

    await call.bot.send_photo(chat_id=call.from_user.id,
                              photo=InputFile(path_or_bytesio=dict_img[type_tovar]),
                              caption='\n\n'.join(list_item), reply_markup=buy)
