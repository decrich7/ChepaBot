# -*- coding: utf-8 -*-


from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from keyboards.inline.menu import catalog
from loader import dp


@dp.message_handler(Command("exit"), state=None)
async def exit_state(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer('Чтобы перейти в меню админа, нажмите /admin')