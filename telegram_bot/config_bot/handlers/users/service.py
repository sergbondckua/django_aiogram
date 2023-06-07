from aiogram.types import ChatType, Message, ChatActions
from aiogram.utils.markdown import hbold, hcode, quote_html, text

from telegram_bot.config_bot.loader import dp


@dp.message_handler(commands=["myid", "my_id"])
async def my_id(message: Message):
    """Return ID information"""

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
