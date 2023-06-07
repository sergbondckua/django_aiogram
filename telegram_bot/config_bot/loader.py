import logging

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage2

from django.conf import settings

from telegram_bot.config_bot.handlers import user

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG if settings.DEBUG else logging.INFO,
)
logger = logging.getLogger(__name__)

bot = Bot(token=settings.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = RedisStorage2() if settings.USE_REDIS else MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Start all handlers
user.register_user_handlers(dp)
