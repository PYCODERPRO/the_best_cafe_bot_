from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.default.menu_uchun import tasdiqlash_buttons,menu_buttons
from loader import dp, bot
from aiogram.types import ReplyKeyboardRemove
from states.holatlar import Forma

# Echo bot
@dp.message_handler(text="Adminga murojaat")
async def bot_echo(message: types.Message):
    await message.answer(text="Ismingizni kiriting",reply_markup=ReplyKeyboardRemove())
    await Forma.ism_qabul_qilish.set()

@dp.message_handler(state=Forma.ism_qabul_qilish,commands="start")
async def bot_echo(message: types.Message,state:FSMContext):
    await message.answer(text="Bosh menyu",reply_markup=menu_buttons)


@dp.message_handler(state=Forma.ism_qabul_qilish)
async def bot_echo(message: types.Message,state:FSMContext):
    ism = message.text
    await state.update_data({'name':ism})
    await message.answer(text="Familyangizni kiriting")
    await Forma.fam_qabul_qilish.set()


# Echo bot
@dp.message_handler(state=Forma.fam_qabul_qilish)
async def bot_echo(message: types.Message,state:FSMContext):
    fam = message.text
    await state.update_data({'surname':fam})
    await message.answer(text="Yoshingizni kiriting kiriting")
    await Forma.yosh_qabul_qilish.set()


# Echo bot
@dp.message_handler(state=Forma.yosh_qabul_qilish)
async def bot_echo(message: types.Message,state:FSMContext):
    yosh = message.text
    await state.update_data({'age':yosh})
    await message.answer(text="Manzilingizni kiriting")
    await Forma.manzil_qabul_qilish.set()


# Echo bot
@dp.message_handler(state=Forma.manzil_qabul_qilish)
async def bot_echo(message: types.Message, state: FSMContext):
        manzil = message.text
        await state.update_data({'location': manzil})
        await message.answer(text="Murojaatingizni kiriting")
        await Forma.murojaat_qabul_qilish.set()


@dp.message_handler(state=Forma.murojaat_qabul_qilish)
async def bot_echo(message: types.Message,state:FSMContext):
    text = message.text
    await state.update_data({'matn':text})
    malumotlar = await state.get_data()
    user_ismi = malumotlar.get('name')
    user_fam = malumotlar.get('surname')
    user_yosh = malumotlar.get('age')
    user_manzil = malumotlar.get('location')
    user_murojaat = malumotlar.get('matn')

    malumot = f"Ism : {user_ismi}\n"\
              f"Familiya : {user_fam}\n" \
              f"Yosh : {user_yosh}\n" \
              f"Manzil : {user_manzil}\n\n" \
              f"Murojaat : {user_murojaat}\n"
    await message.answer(text=malumot,reply_markup=tasdiqlash_buttons)

    await Forma.tasdiqlash_holati.set()

@dp.message_handler(state=Forma.tasdiqlash_holati,text="tasdiqlayman✅")
async def bot_echo(message: types.Message, state: FSMContext):
    malumotlar = await state.get_data()
    user_ismi = malumotlar.get('name')
    user_fam = malumotlar.get('surname')
    user_yosh = malumotlar.get('age')
    user_manzil = malumotlar.get('location')
    user_murojaat = malumotlar.get('matn')

    malumot = f"Ushbu {message.from_user.first_name} foydalanuvchi sizga murojaat yubordi\n\n"\
              f"Ism : {user_ismi}\n" \
              f"Familiya : {user_fam}\n" \
              f"Yosh : {user_yosh}\n" \
              f"Manzil : {user_manzil}\n\n" \
              f"Murojaat : {user_murojaat}\n"

    await bot.send_message(chat_id="5836492286",text=malumot)
    await message.answer(text="Murojaatingiz adminga yuborildi✅",reply_markup=menu_buttons)
    await state.finish()


@dp.message_handler(state=Forma.tasdiqlash_holati,text="bekor qilaman, jo'natilmasin❌")
async def bot_echo(message: types.Message, state: FSMContext):

    await message.answer(text="murojaat jo'natilmadi❌",reply_markup=menu_buttons)
    await state.finish()




















