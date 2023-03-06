# -*- coding: utf-8 -*-

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

#
# catalog = InlineKeyboardMarkup(inline_keyboard=[
#     [
#         InlineKeyboardButton(text="📁 Каталог 📁", callback_data="menu")
#     ]
# ])

catalog = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="📱 iPhone 📱", callback_data="tovar_iphone"),
        InlineKeyboardButton(text="💻 MacBook 💻", callback_data="tovar_macbook"),
        InlineKeyboardButton(text="📱 iPad 📱", callback_data="tovar_ipad")

    ],
    [
        InlineKeyboardButton(text="⌚️ Apple Watch ⌚️", callback_data="tovar_apple watch"),
        InlineKeyboardButton(text="🎧 AirPods 🎧", callback_data="tovar_airpods"),

    ],
    [
        InlineKeyboardButton(text="🔊 Музыкальные станции 🔊", callback_data="tovar_music"),
        InlineKeyboardButton(text="🎮 Игровые приставки 🎮", callback_data="tovar_game")
    ]
])

buy = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🛒 Купить 🛒", url='https://t.me/a_chepulchenko')
    ]
])
