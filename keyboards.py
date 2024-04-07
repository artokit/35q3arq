import json

from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton


def create_keyboard(func):
    def wrapper():
        keyboard = InlineKeyboardBuilder()
        func(keyboard)
        return keyboard.as_markup()

    return wrapper


@create_keyboard
def admin(keyboard: InlineKeyboardBuilder):
    keyboard.row(InlineKeyboardButton(text="Изменить приветственное сообщение", callback_data="change_hello"))
    keyboard.row(InlineKeyboardButton(text="Изменить инвайт ссылку", callback_data="change_invite"))
    keyboard.row(InlineKeyboardButton(
        text="Изменить сообщение после вступления в группу",
        callback_data="change_second"
        )
    )


@create_keyboard
def start(keyboard: InlineKeyboardBuilder):
    keyboard.row(InlineKeyboardButton(text="🚀НАЧАТЬ🚀", url=json.load(open("admin_settings.json"))['url']))


@create_keyboard
def invite(keyboard: InlineKeyboardBuilder):
    keyboard.row(InlineKeyboardButton(text="🚀ЗАЙТИ В КАНАЛ🚀", url=json.load(open("admin_settings.json"))['url']))
