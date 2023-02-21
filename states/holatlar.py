from aiogram.dispatcher.filters.state import State, StatesGroup

class Forma(StatesGroup):
    ism_qabul_qilish = State()
    fam_qabul_qilish = State()
    yosh_qabul_qilish = State()
    manzil_qabul_qilish = State()
    murojaat_qabul_qilish = State()
    tasdiqlash_holati = State()
