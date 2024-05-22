from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from aiogram.utils.markdown import hbold,hcode,hitalic,hunderline,hlink,hstrikethrough
from loader import dp

@dp.message_handler(commands='info_html')
async def bot_help(message: types.Message):
    text=f"Assalomu aleykum {message.from_user.full_name}!\n"
    text+='Bu <b> qalin </b> shrift'
    text += 'Bu <i> qalin </i> shrift'
    text += 'Bu <u> qalin </u> shrift'
    text += 'Bu <s> qalin </s> shrift'
    text += "Bu <a href='https://kun.uz'> Kun uz sahifasi </a>"
    text += "Bu kod: <code> print('Salom') </code>"

    await message.answer(text)


@dp.message_handler(commands='info_markdown')
async def get_mark(message: types.Message):
    text=f"Assalomu aleykum {message.from_user.full_name}!\n"
    text+=f"Bu *Qalin shrift markdown usulida*"
    text+=f"~to'lqin~"
    text+=f"[Kun uz sahifasi]( https://kun.uz)"

    await message.answer(text, parse_mode=types.ParseMode.MARKDOWN_V2)