from aiogram import types
from aiogram.types import ContentTypes
from aiogram.types import InputFile
from loader import dp,bot


# Echo bot
@dp.message_handler(text="gamburger")
async def bot_echo(message: types.Message):
    rasm_manzil = "https://t.me/media_uchun596/6"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzil,caption="Fast food taomlardan biri gamburger\n"
                                                                                              "narxi:22000\n"
                                                                                              "eltib berish : 8000\n"
                                                                                               "hammasi bo'lib 30000")


# Echo bot
@dp.message_handler(text="sho'rva")
async def bot_echo(message: types.Message):
    rasm_manzil = "https://t.me/media_uchun596/9"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzil,caption="Bu sho'rva\n"
                                                              "narxi:12000\n"
                                                               "eltib berish : 8000\n"
                                                                "hammasi bo'lib : 28000")

# Echo bot
@dp.message_handler(text="osh")
async def bot_echo(message: types.Message):
    rasm_manzil = "https://t.me/media_uchun596/16"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzil,caption="Bu osh\n"
                                                              "narxi : 15000\n"
                                                               "eltib berish : 8000\n"
                                                                "hammasi bo'lib : 23000")


# Echo bot
@dp.message_handler(text="somsa")
async def bot_echo(message: types.Message):
    rasm_manzil = "https://t.me/media_uchun596/14"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzil,caption="Bu somsa\n"
                                                              "narxi : 10000\n"
                                                               "eltib berish : 8000\n"
                                                                "hammasi bo'lib : 18000")


# Echo bot
@dp.message_handler(text="pizza")
async def bot_echo(message: types.Message):
    rasm_manzil = "https://t.me/media_uchun596/10"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzil,caption="Bu pizza\n"
                                                              "narxi : 30000\n"
                                                               "eltib berish : 8000\n"
                                                                "hammasi bo'lib : 38000")


# Echo bot
@dp.message_handler(text="xot dog")
async def bot_echo(message: types.Message):
    rasm_manzil = "https://t.me/media_uchun596/3"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzil,caption="Bu xot dog\n"
                                                              "narxi : 11000\n"
                                                               "eltib berish : 8000\n"
                                                                "hammasi bo'lib : 19000")

# Echo bot
@dp.message_handler(text="lag'mon")
async def bot_echo(message: types.Message):
    rasm_manzil = "https://t.me/media_uchun596/26"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzil,caption="Bulag'mon\n"
                                                              "narxi : 15000\n"
                                                               "eltib berish : 8000\n"
                                                                "hammasi bo'lib : 23000")

# Echo bot
@dp.message_handler(text="chuchvara")
async def bot_echo(message: types.Message):
    rasm_manzil = "https://t.me/media_uchun596/27"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzil,caption="Bu chuchvara\n"
                                                              "narxi : 18000\n"
                                                               "eltib berish : 8000\n"
                                                                "hammasi bo'lib : 26000")





































