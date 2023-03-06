from aiogram import Bot
async def checking(user_id,kanal_link):
    user = Bot.get_current()
    tek = await user.get_chat_member(chat_id=kanal_link,user_id=user_id)
    return tek.is_chat_member()


