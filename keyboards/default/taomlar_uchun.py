from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

taomlar_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [

        ],
        [
            KeyboardButton(text="sho'rva"),
            KeyboardButton(text="osh"),
        ],
        [
            KeyboardButton(text="somsa"),
            KeyboardButton(text="lag'mon"),
        ],
        [
            KeyboardButton(text="chuchvara"),
            KeyboardButton(text="mastava")
        ],
        [
            KeyboardButton(text="ortga🔙"),
        ]
    ],
    resize_keyboard=True
)
fast_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="gamburger"),
            KeyboardButton(text="pizza"),
            KeyboardButton(text="xot dog")
        ],
        [
            KeyboardButton(text='ortga🔙')
        ]
    ],
    resize_keyboard=True
)
