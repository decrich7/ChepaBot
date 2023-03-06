# -*- coding: utf-8 -*-

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


crud_admin = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Удалить товар", callback_data="remove")

    ],
    [
        InlineKeyboardButton(text="Изменить товар", callback_data="change")

    ],
    [
        InlineKeyboardButton(text="Добавить Товар", callback_data="add")
    ]
])

buy = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🛒 Купить 🛒", url='https://t.me/a_chepulchenko')
    ]
])

change_tovar = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Изменить название товара", callback_data="change_name")

    ],
    [
        InlineKeyboardButton(text="Изменить цену", callback_data="change_price")

    ]
])
