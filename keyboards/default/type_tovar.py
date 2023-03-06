# -*- coding: utf-8 -*-


from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# menu = ReplyKeyboardMarkup(
#     keyboard=[
#         [
#             KeyboardButton(text="Котлетки"),
#         ],
#         [
#             KeyboardButton(text="Макарошки"),
#             KeyboardButton(text="Пюрешка")
#         ],
#     ],
#     resize_keyboard=True
# )


type_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📱 iPhone 📱"),
            KeyboardButton(text="💻 MacBook 💻"),
            KeyboardButton(text="📱 iPad 📱")

        ],
        [
            KeyboardButton(text="⌚️ Apple Watch ⌚️"),
            KeyboardButton(text="🎧 AirPods 🎧"),

        ],
        [
            KeyboardButton(text="🔊 Музыкальные станции 🔊"),
            KeyboardButton(text="🎮 Игровые приставки 🎮")
        ],
        [
            KeyboardButton(text="❌ Отмена ❌")
        ]
    ],
    resize_keyboard=True
)

