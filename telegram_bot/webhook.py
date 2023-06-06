from aiogram import types, Bot, Dispatcher

from telegram_bot.config_bot.loader import bot, dp


async def proceed_update(request: dict):
    """
    Processes the update received and sends the appropriate response.
    """
    update = types.Update(**request)
    Dispatcher.set_current(dp)
    Bot.set_current(bot)
    await dp.process_update(update)
