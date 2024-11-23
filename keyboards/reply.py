from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, KeyboardButtonPollType

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📜 Меню"),
            KeyboardButton(text="👀 Про нас"),
        ],
        [
            KeyboardButton(text="🚚 Доставка"),
            KeyboardButton(text="💳 Варіанти оплати"),
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder='Час купувати'
)

delivery_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="???", request_poll=KeyboardButtonPollType()),
        ],
        [
            KeyboardButton(text="📞 Телефон", request_contact=True),
            KeyboardButton(text="📍 Розташування", request_location=True),
        ]
    ]
)

del_kb = ReplyKeyboardRemove()
