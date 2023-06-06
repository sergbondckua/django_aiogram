from aiogram import types
from aiogram.dispatcher.filters import CommandStart, CommandHelp
from aiogram.utils.markdown import hbold, text, hcode, hitalic

from telegram_bot.config_bot.loader import dp, bot


@dp.message_handler(CommandStart())
async def cmd_start(message: types.Message):
    """ Mandatory command /start """
    bot_username = (await bot.me).username
    txt = text(
        text(hitalic("i'm a bot"), hitalic(bot_username)),
        text("Hello", hbold(message.from_user.full_name), "!"),
        sep="\n",
    )
    await message.answer(text=txt)


@dp.message_handler(CommandHelp())
async def cmd_help(message: types.Message):
    """ Mandatory command /help """
    txt = text(
        text(hbold("Under construction")),
        text(hcode("Python"), hcode(message.from_user.mention)),
        sep="\n",
    )
    await message.answer(text=txt)
