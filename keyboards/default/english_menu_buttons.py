from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

eng_menu_buttons = ReplyKeyboardMarkup(
    keyboard=[
       [
           KeyboardButton(text="national dishes"),
           KeyboardButton(text="fast food🍟")
       ],
       [
           KeyboardButton(text="Contact admin👨🏻‍💻")
       ],
       [
            KeyboardButton(text=" my number📞",request_contact=True),
            KeyboardButton(text="my location📍",request_location=True)
       ],
       [
            KeyboardButton(text="Drinks"),
            KeyboardButton(text="Sweets")
        ]
    ],
    resize_keyboard=True
)
tasdiqlash_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="OK✅"),
            KeyboardButton(text="Cancel❌")
        ]
    ],
    resize_keyboard=True
)