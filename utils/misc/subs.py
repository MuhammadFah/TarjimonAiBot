from data.config import channels
from loader import bot


async def check_subs_channel(message):
    for channel in channels:
        check = await bot.get_chat_member(channel[1], message.from_user.id)
        if check.status == "left":
            return False

    return True