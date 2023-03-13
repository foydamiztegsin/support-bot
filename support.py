

import logging
from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.filters import Command
from aiogram.types import ParseMode
import os
from dotenv import load_dotenv

# Loglar uchun
logging.basicConfig(level=logging.INFO)
load_dotenv()

# Botni yaratish
API_TOKEN = os.getenv('API_TOKEN')
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Admin chat id si bilan ishlash uchun o'zgaruvchi
ADMIN_ID = os.getenv('ADMIN_ID')



@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply(" Assalomu alaykum! Men xabarlarini qabul qiluvchi botman. Marhamat, menga xabaringizni yuboring. Bir ozdan so'ng, admin sizga javob jo'natadi.")
# Botga yozilgan har bir xabarga javob berish

# Admin javoblari
@dp.message_handler(Command('reply'), user_id=ADMIN_ID)
async def reply(message: types.Message):
    # Xabar ma'nosi va qabul qiluvchi foydalanuvchi id sini olish
    text = message.get_args()
    user_id = int(text.split(' ')[0])

    # Javob xabarni olish va javob yozish
    reply_text = ' '.join(text.split(' ')[1:])
    await bot.send_message(chat_id=user_id, text=reply_text, parse_mode=ParseMode.HTML)


@dp.message_handler()
async def echo(message: types.Message):
    # Xabar matnini olish
    text = message.text

    # Foydalanuvchi xabarni yuborgan
    user_id = message.from_user.id

    # Xabarni admin ga yuborish
    await bot.send_message(chat_id=ADMIN_ID, text=f'Foydalanuvchi {user_id} botga yozdi: \n\n{text}')

    # Javob yozish
    await message.reply('Sizning xabaringiz yetkazildi. Tez orada javob olasiz. Rahmat!')




if __name__ == '__main__':
    
    # Botni ishga tushirish
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
