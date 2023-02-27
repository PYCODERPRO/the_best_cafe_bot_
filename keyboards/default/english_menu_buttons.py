from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

eng_menu_buttons = ReplyKeyboardMarkup(
    keyboard=[
       [
           KeyboardButton(text="national dishes"),
           KeyboardButton(text="fast foods")
       ],
       [
           KeyboardButton(text="Admin")
       ],
       [
            KeyboardButton(text=" my number",request_contact=True),
            KeyboardButton(text="my location",request_location=True)
       ],
       [
            KeyboardButton(text="drinks"),
            KeyboardButton(text="sweets")
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