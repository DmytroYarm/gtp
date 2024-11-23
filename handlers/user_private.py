from aiogram import F, types, Router
from aiogram.filters import CommandStart, Command, or_f

from filters.chat_types import ChatTypeFilter

user_privat_router = Router()
user_privat_router.message.filter(ChatTypeFilter(["private"]))


@user_privat_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer("🐍 hello_new_user 🐍")


@user_privat_router.message(Command("shh"))
async def start_cmd(message: types.Message):
    await message.answer("🐍 Don't tell anyone about it 🐍")


@user_privat_router.message(F.text.lower().contains('меню'))
@user_privat_router.message(Command("menu"))
async def start_cmd(message: types.Message):
    await message.answer("🐍 menu here 🐍")


@user_privat_router.message(Command("about"))
async def start_cmd(message: types.Message):
    await message.answer("🐍 We are your new way 🐍")


@user_privat_router.message(or_f(Command("payment"), F.text.lower().contains('оплата')))
async def start_cmd(message: types.Message):
    await message.answer("🐍 Give me your money 🐍")


@user_privat_router.message(Command("shipping"))
async def start_cmd(message: types.Message):
    await message.answer("🐍 Take your order 🐍")


@user_privat_router.message((F.text.lower().contains('hi')) | (F.text.lower().contains('hello')))
async def echo_cmd(message: types.Message):
    # text = message.text.lower()
    # if text in ["hello", "hi", "привет", "ку"]:
    #     await message.answer("Sshhh...Hello, my friend!!")
    # elif text in ["bye", "goodbye", "пока"]:
    #     await message.answer("Bye-bye! See you later")
    # else:
    #     await message.answer("I dont think I understand what you mean")

    await message.answer("💫 Magic 🪄")
