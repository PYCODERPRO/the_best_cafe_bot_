from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from data.config import kanallar
from data.tekshirish import checking
from loader import bot



class Asosiy_checking(BaseMiddleware):
    async def on_pre_process_update(self,xabar:types.Update,data:dict):
        if xabar.message:
            user_id = xabar.message.from_user.id
        elif xabar.callback_query:
            user_id = xabar.callback_query.from_user.id
        else:
            return
        matn = "Quydagi kanalga azo boling\n"
        royxat = []
        daslabki_holati = True
        for k in kanallar:
            holat = await checking(user_id=user_id,kanal_link=k)
            daslabki_holati *= holat

            kanal = await bot.get_chat(k)

            if not holat:
                link = await kanal.export_invite_link()
                button = [InlineKeyboardButton(text=f"Obuna bolish",url=f"{link}")]
                royxat.append(button)
        royxat.append([InlineKeyboardButton(text="Tekshirish",callback_data="www")])
        if not daslabki_holati:
            await bot.send_message(chat_id=xabar.message.chat.id,text=matn,disable_web_page_preview=True,
                                   reply_markup=InlineKeyboardMarkup(inline_keyboard=royxat))
            await bot.ban_chat_sender_chat(chat_id=xabar.message.chat.id,sender_chat_id=xabar.message.from_user.id)
            raise CancelHandler()