from aiogram import F, types, Router
from aiogram.filters import CommandStart, Command, or_f

from filters.chat_types import ChatTypeFilter
from keyboards import reply

user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter(["private"]))


@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer("🐍 hello_new_user 🐍", reply_markup=reply.start_kb)


@user_private_router.message(Command("shh"))
async def start_cmd(message: types.Message):
    await message.answer("🐍 Don't tell anyone about it 🐍")


@user_private_router.message(F.text.lower().contains('меню'))
@user_private_router.message(Command("menu"))
async def start_cmd(message: types.Message):
    await message.answer("🐍 menu here 🐍", reply_markup=reply.del_kb)


@user_private_router.message(Command("about"))
async def start_cmd(message: types.Message):
    await message.answer("🐍 We are your new way 🐍")


@user_private_router.message(or_f(Command("payment"), F.text.lower().contains('оплата')))
async def start_cmd(message: types.Message):
    await message.answer("🐍 Give me your money 🐍")


@user_private_router.message(Command("shipping"))
async def start_cmd(message: types.Message):
    await message.answer("🐍 Take your order 🐍")


@user_private_router.message((F.text.lower().contains('hi')) | (F.text.lower().contains('hello')))
async def echo_cmd(message: types.Message):
    # text = message.text.lower()
    # if text in ["hello", "hi", "привет", "ку"]:
    #     await message.answer("Sshhh...Hello, my friend!!")
    # elif text in ["bye", "goodbye", "пока"]:
    #     await message.answer("Bye-bye! See you later")
    # else:
    #     await message.answer("I dont think I understand what you mean")

    await message.answer("💫 Magic 🪄")


@user_private_router.message(F.contact)
async def get_contact(message: types.Message):
    await message.answer(f"контакти отримані")
    await message.answer(str(message.contact))

@user_private_router.message(F.location)
async def get_location(message: types.Message):
    await message.answer(f"локація отримана")
    await message.answer(str(message.location))
