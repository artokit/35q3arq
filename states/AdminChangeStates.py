from aiogram.fsm.state import StatesGroup, State


class AdminChangeStates(StatesGroup):
    hello_message_change = State()
    change_invite = State()
    change_invite_message = State()
