import logging

from aiogram import Dispatcher



async def on_startup_notify(dp: Dispatcher):
    try:
        await dp.bot.send_message(778981429, "Бот Запущен")

    except Exception as err:
        logging.exception(err)
