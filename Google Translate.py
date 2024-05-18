from googletrans import Translator
from aiogram import executor, types, Bot, Dispatcher
import logging

API_TOKEN = "6724863929:AAFZIVixjZhxGtM8sPKgTXKMaO7bP_Pn2E8"
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
translator = Translator()

@dp.message_handler(commands=['start', 'help'])
async def hello(message: types.Message):
    await message.answer('Assalom aleykum botga hush kelibsiz')

@dp.message_handler()
async def get_data(message: types.Message):
    translation = translator.translate(message.text, dest='en')
    translated_text = translation.text
    await message.reply(translated_text)

if name == 'main':
    executor.start_polling(dp, skip_updates=True)