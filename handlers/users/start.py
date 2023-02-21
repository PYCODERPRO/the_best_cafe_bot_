from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.menu_uchun import menu_buttons
from keyboards.default.taomlar_uchun import taomlar_buttons
from keyboards.inline.tillar_uchun import tillar_buttons
from keyboards.default.taomlar_uchun import fast_buttons
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Assalomu Alaykum hurmatli foydalanuvchi, {message.from_user.full_name}!",reply_markup=tillar_buttons)


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!",reply_markup=menu_buttons)


@dp.message_handler(text='milliy taomlar')
async def bot_start(message: types.Message):
    await message.answer(f"milliy taomlarni tanlang",reply_markup=taomlar_buttons)

@dp.message_handler(text='fast food')
async def bot_start(message: types.Message):
    await message.answer(f"fast food taomlardan birini tanlang, {message.from_user.full_name}!",reply_markup=fast_buttons)

@dp.message_handler(text="O'zbek tili")
async def bot_start(message: types.Message):
    await message.answer(f"fast food taomlardan birini tanlang, {message.from_user.full_name}!",reply_markup=menu_buttons)


@dp.message_handler(text='ortga🔙')
async def bot_start(message: types.Message):
    await message.answer(f"fast food taomlarni tanlang!",reply_markup=menu_buttons)

