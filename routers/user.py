import json
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, ChatJoinRequest
import config
import keyboards
from database import db_api
from keitaro_api import ApiService

router = Router()


@router.message(Command("start"))
async def start(message: Message):
    utm = "null"

    if " " in message.text:
        utm = message.text.split(" ")[1]

    db_api.add_user(message.chat.id, message.chat.username, utm)
    data = json.loads(open("admin_settings.json", 'rb').read().decode())
    await ApiService.send_start(utm, message.chat.id)
    await message.answer_video(video=data["file_id"], caption=data["caption"], reply_markup=keyboards.start())
    await message.bot.send_message(config.NOTIFICATION_CHANNEL, f"{message.chat.id}:{utm}:start")


@router.chat_join_request()
async def auto_approve_member(update: ChatJoinRequest):
    if update.chat.id == config.APPROVE_CHANNEL_ID:
        await update.approve()
        utm = db_api.get_user(update.from_user.id)[2]
        await update.bot.send_message(config.NOTIFICATION_CHANNEL, f"{update.from_user.id}:{utm}:sign-up")
        data = json.loads(open("admin_settings.json", 'rb').read().decode())
        await update.bot.send_video(chat_id=update.from_user.id, video=data["approve_video_file_id"], caption=data["approve_video_caption"], reply_markup=keyboards.invite())
        await ApiService.send_status(utm, "sign-up")
