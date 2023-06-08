from aiogram import Dispatcher
from aiogram.types import Message, ChatActions, ChatType
from aiogram.dispatcher.filters import CommandHelp, CommandStart
from aiogram.utils.markdown import text, hitalic, hbold, hcode, quote_html

from django.utils.translation import gettext_lazy as _


async def cmd_start(message: Message):
    """
    Mandatory command /start
    Обов'язкова команда /start
    """
    msg = text(
        text(hitalic(_("i'm a bot"))),
        text(_("Hello"), hbold(message.from_user.full_name), "!"),
        sep="\n",
    )
    await message.answer(text=msg)


async def cmd_help(message: Message):
    """
    Mandatory command /help
    Обов'язкова команда /help
    """
    msg = text(
        text(hbold(_("Under construction"))),
        text(hcode(_("Python")), hcode(message.from_user.mention)),
        sep="\n",
    )
    await message.answer(text=msg)


async def cmd_info_id(message: Message):
    """
    Return user ID information
    Повертає ID-інфо користувача
    """

    full_name = message.from_user.full_name
    userid = message.from_user.id
    chat_id = message.chat.id
    username = message.from_user.mention if message.from_user.mention else "➖"
    if message.chat.type != ChatType.PRIVATE:
        title = message.chat.title
    else:
        title = full_name
    msg = text(
        hbold(_("Your ID information:")),
        text("🚻", hbold(_("Full name:")), quote_html(full_name)),
        text("🪪", hbold(_("Username:")), quote_html(username)),
        text("🆔", hbold(_("Your ID:")), hcode(userid)),
        text("💬", hbold(_("Chat ID:")), hcode(chat_id)),
        text("🔸", hbold(_("Title:")), hcode(title)),
        sep="\n",
    )
    await ChatActions.typing()
    await message.answer(text=msg)


def register_user_handlers(dp: Dispatcher):
    """Register all handlers"""
    dp.register_message_handler(cmd_start, CommandStart(), state="*")
    dp.register_message_handler(cmd_help, CommandHelp(), state="*")
    dp.register_message_handler(cmd_info_id, commands=["myid"], state="*")
