from aiogram import F, types, Router
from aiogram.filters import CommandStart, Command, or_f
from aiogram.types import InputFile, FSInputFile
from aiogram.utils.formatting import as_list, as_marked_section, Bold
from google.oauth2 import service_account
from googleapiclient.discovery import build

from filters.chat_types import ChatTypeFilter
from keyboards import reply

user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter(["private"]))





# SCOPES = ['https://www.googleapis.com/auth/documents.readonly']
# DOCUMENT_ID = '10CRiHLDDoa8x6pQcktVKwHveOL8VdJPN6P_gHDfUdWo'
# SERVICE_ACCOUNT_FILE = '/Users/main/Downloads/gtp-course-fb0abae1add2.json'
#
# credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
# service = build('docs', 'v1', credentials=credentials)
#
# def get_document_text():
#     document = service.documents().get(documentId=DOCUMENT_ID).execute()
#     content = document.get('body').get('content')
#     text = ''
#     for element in content:
#         if 'paragraph' in element:
#             paragraph_elements = element.get('paragraph').get('elements')
#             for elem in paragraph_elements:
#                 if 'textRun' in elem:
#                     text += elem.get('textRun').get('content')
#     return text


photo_path = "/Users/main/Downloads/taurus.jpg"



@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer("🐍 hello_new_user 🐍", reply_markup=reply.start_kb)


@user_private_router.message(Command("shh"))
async def shh_cmd(message: types.Message):
    await message.answer_photo(photo=FSInputFile(photo_path), )


@user_private_router.message(F.text.lower().contains('меню'))
@user_private_router.message(Command("menu"))
async def menu_cmd(message: types.Message):
    await message.answer("🐍 menu here 🐍", reply_markup=reply.del_kb)


@user_private_router.message(Command("about"))
async def about_cmd(message: types.Message):
    await message.answer("🐍 We are your new way 🐍")


@user_private_router.message(or_f(Command("payment"), F.text.lower().contains('оплата')))
async def payment_cmd(message: types.Message):
    await message.answer("🐍 Give me your money 🐍")


@user_private_router.message(Command("shipping"))
async def shipping_cmd(message: types.Message):
    text = as_list(
        as_marked_section(
            Bold("Варіанти оплати\n"),
            "На карту",
            "Накладений платіж",
            "При отриманні",
            marker="🟢 "
        ),
        as_marked_section(
            Bold("Відсутня можливість\n"),
            "Голубом",
            "Совою",
            "Авіацією",
            marker="⛔️ "
        ),
        sep="\n----------------------------\n"
    )
    await message.answer(text.as_html())


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
