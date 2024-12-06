from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, KeyboardButtonPollType

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📜 Теорія"),
            KeyboardButton(text="👀 Практика"),
        ],
        [
            KeyboardButton(text="📻 Зв'язок з нами"),
            # KeyboardButton(text="💳 Контакти"),
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
