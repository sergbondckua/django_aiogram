from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import Message, ChatActions, ChatType
from aiogram.utils.markdown import text, hitalic, hbold, hcode, quote_html

from django.utils.translation import gettext_lazy as _

from telegram_bot.config_bot.misc.states import Test
# from telegram_bot.config_bot.loader import dp


# @dp.message_handler(Command("test"), state=None)
async def enter_test(message: Message, state: FSMContext):
    await state.finish()  # Завершаем предыдущее состояние, если оно существует
    await message.answer("Вы начали тестирование.\n"
                         "Вопрос №1. \n\n"
                         "Вы часто занимаетесь бессмысленными делами "
                         "(бесцельно блуждаете по интернету, клацаете пультом телевизора, просто смотрите в потолок)?")

    await Test.Q1.set()


# @dp.message_handler(state=Test.Q1)
async def answer_q1(message: Message, state: FSMContext):
    answer = message.text

    # We store the answer in the key=var variable
    # Зберігаємо відповідь в змінну key=var
    await state.update_data(answer1=answer)
    await message.answer("Вопрос №2. \n\n"
                         "Ваша память ухудшилась и вы помните то, что было давно, но забываете недавние события?")
    await Test.Q2.set()


# @dp.message_handler(state=Test.Q2)
async def answer_q2(message: Message, state: FSMContext):
    # Отримаємо відповіді
    data = await state.get_data()
    answer1 = data.get("answer1")
    answer2 = message.text

    await message.answer("Спасибо за ваши ответы! \n" + answer1 + " " + answer2)
    await state.finish()


def register_testing_handlers(dp: Dispatcher):
    """Register all handlers"""

    dp.register_message_handler(enter_test, commands=["test"], state="*")
    dp.register_message_handler(answer_q1, state=Test.Q1)
    dp.register_message_handler(answer_q2, state=Test.Q2)
