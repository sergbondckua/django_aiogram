from aiogram import Dispatcher
from aiogram.types import Message, ChatActions, ChatType
from aiogram.utils.markdown import text, hitalic, hbold, hcode, quote_html


async def cmd_start(message: Message):
    """ Mandatory command /start """
    txt = text(
        text(hitalic("i'm a bot")),
        text("Hello", hbold(message.from_user.full_name), "!"),
        sep="\n",
    )
    await message.answer(text=txt)


async def cmd_help(message: Message):
    """ Mandatory command /help """
    txt = text(
        text(hbold("Under construction")),
        text(hcode("Python"), hcode(message.from_user.mention)),
        sep="\n",
    )
    await message.answer(text=txt)


async def cmd_info_id(message: Message):
    """Return user ID information"""

    full_name = message.from_user.full_name
    userid = message.from_user.id
    chat_id = message.chat.id
    username = message.from_user.mention if message.from_user.mention else "➖"
    if message.chat.type != ChatType.PRIVATE:
        title = message.chat.title
    else:
        title = full_name
    txt = text(
        hbold("Your ID information:"),
        text("🚻", hbold("Full name:"), quote_html(full_name)),
        text("🪪", hbold("Username:"), quote_html(username)),
        text("🆔", hbold("Your ID:"), hcode(userid)),
        text("💬", hbold("Chat ID:"), hcode(chat_id)),
        text("🔸", hbold("Title:"), hcode(title)),
        sep="\n",
    )
    await ChatActions.typing()
    await message.answer(text=txt)


def register_user_handlers(dp: Dispatcher):
    """Register all handlers"""
    dp.register_message_handler(cmd_start, commands=["start"], state="*")
    dp.register_message_handler(cmd_help, commands=["help"], state="*")
    dp.register_message_handler(cmd_info_id, commands=["myid"], state="*")
