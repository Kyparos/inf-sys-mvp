from aiogram.dispatcher.filters.state import State, StatesGroup


class BotStates(StatesGroup):
    main_menu = State()
    gender_menu = State()
    cp_menu = State()