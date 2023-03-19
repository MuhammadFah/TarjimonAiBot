from aiogram import Dispatcher
from aiogram.types import *

from database.connections import add_user
from keyboards.inline.channels import show_channels
from keyboards.inline.users_btn import languages_btn
from loader import dp
from utils.misc.text_translator import text_trans
from utils.misc.subs import check_subs_channel


async def bot_start(message: Message):
    user = message.from_user.id
    username = message.from_user.username
    await add_user(user, username)
    check = await check_subs_channel(message)
    if check:
        await message.answer(f"Assalomu aleykom")
    else:
        btn = await show_channels()
        msg = f"Xurmatli <b>{message.from_user.full_name}</b>\nBotdan Foydalanishdan avval quyidagi kanallarga obuna bo`ling"
        await message.answer(msg, reply_markup=btn)


async def check_subscription(call: CallbackQuery):
    check = await check_subs_channel(call)
    if check:
        await call.message.edit_text("Siz Kanallarga Obuna bo`lmayabsiz")
    else:
        await call.answer("Siz Berilgan Kanallarga Obuna Bo`ling", show_alert=True)


async def get_user_text_handler(message: Message):
    check = await check_subs_channel(message)
    if check:
        text = message.text
        btn = await languages_btn()
        await message.answer(text, reply_markup=btn)
    else:
        btn = await show_channels()
        msg = f"Xurmatli <b>{message.from_user.full_name}</b>\nBotdan Foydalanishdan avval quyidagi kanallarga obuna bo`ling"
        await message.answer(msg, reply_markup=btn)


async def select_lang_callback(call: CallbackQuery):
    await call.answer()
    lang = call.data.split(":")[-1]
    context = call.message.text
    result = await text_trans(context, lang)
    if context != result:
        btn = await languages_btn()
        await call.message.edit_text(result, reply_markup=btn)


def register_users_py(dp: Dispatcher):
    dp.register_message_handler(bot_start, commands=['start'])
    dp.register_message_handler(get_user_text_handler, content_types=['text'])

    dp.register_callback_query_handler(check_subscription, text='sub channel done')
    dp.register_callback_query_handler(select_lang_callback, text_contains='lang:')
