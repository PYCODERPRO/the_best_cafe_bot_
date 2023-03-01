from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu_buttons = ReplyKeyboardMarkup(
    keyboard=[
       [
           KeyboardButton(text="milliy taomlar"),
           KeyboardButton(text="fast food")
       ],
       [
           KeyboardButton(text="Adminga murojaat")
       ],
       [
            # KeyboardButton(text="telefon raqam",request_contact=True),
            # KeyboardButton(text="mening manzilim",request_location=True)
       ],
       [
            KeyboardButton(text="ichimliklar"),
            KeyboardButton(text="shirinliklar")
        ]
    ],
    resize_keyboard=True
)
tasdiqlash_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="tasdiqlayman✅"),
            KeyboardButton(text="bekor qilaman, jo'natilmasin❌")
        ]
    ],
    resize_keyboard=True
)
