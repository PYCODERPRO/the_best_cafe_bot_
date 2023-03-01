from aiogram import types

from loader import dp


# Echo bot
@dp.message_handler(commands="start")
async def bot_echo(message: types.Message):
    await message.answer(text="GURUHGA HUSH KELIBSIZ")
