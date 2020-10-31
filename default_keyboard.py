from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


Country = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='İstanbul'),
            KeyboardButton(text='İzmir')
        ],
        [
            KeyboardButton(text='Antalya')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)