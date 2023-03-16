from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from data.config import channels


async def show_channels():
    keyboard = InlineKeyboardMarkup(row_width=1)

    for channel in channels:
        btn = InlineKeyboardButton(text=channel[0], url=channel[2])
        keyboard.insert(btn)

    done = InlineKeyboardButton(text="Azo Bo`ldim", callback_data="Sub Channel Done")
    keyboard.insert(done)

    return keyboard
