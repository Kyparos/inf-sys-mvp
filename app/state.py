from aiogram.dispatcher.filters.state import State, StatesGroup


class BotStates(StatesGroup):
    main_menu = State()
    gender_menu = State()
    cp_menu = State()
    trtbps_menu = State()
    chol_menu = State()
    #hide_menu = State()
    fbs_menu = State()
    restecg_menu = State()
    thalachh_menu = State()
    exng_menu = State()
    oldpeak_menu = State()
    slp_menu = State()
    caa_menu = State()
    thall_menu = State()
    result = State()
