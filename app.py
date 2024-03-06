import asyncio
from aiogram import F, Bot, types, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.enums import ParseMode
from dotenv import load_dotenv
import os

load_dotenv()
bot = Bot (os.getenv('TOKEN'))
dp = Dispatcher()


@dp.message()
async def start_cmd(message: types.Message):
    await message.answer("Подпишитесь на уведомления от MedHelp24. Для настройки зайдите в свой профиль на сайте medhelp24.com")


async def main():
        await dp.start_polling(bot)

asyncio.run (main())



# # Если не указать фильтр F.text, 
# # то хэндлер сработает даже на картинку с подписью /test
# @dp.message(F.text, Command("test"))
# async def any_message(message: Message):
#     await message.answer(
#         "Hello, <b>world</b>!", 
#         parse_mode=ParseMode.HTML
#     )
#     await message.answer(
#         "Подпишитесь на уведомления от MedHelp24. Для настройки зайдите в свой профиль на сайте medhelp24.com", 
#         parse_mode=ParseMode.MARKDOWN_V2
