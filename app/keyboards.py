from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

import locale_


def create_menu(variants_dict):
    return ReplyKeyboardMarkup([[KeyboardButton(k) for k in variants_dict.keys()]], resize_keyboard=True)

class Keyboards:


    MainMenu = create_menu(locale_.main_menu)

    GenderMenu = create_menu(locale_.gender_menu)

    CpMenu = create_menu(locale_.cp_menu)

    TrtbpsMenu = create_menu(locale_.trtbps_menu)

    CholMenu = create_menu(locale_.chol_menu)


    FbsMenu = create_menu(locale_.fbs_menu)


    RestecgMenu = create_menu(locale_.restecg_menu)

    ThalachhMenu = create_menu(locale_.thalachh_menu)

    ExngMenu = create_menu(locale_.exng_menu)

    OldpeakMenu = create_menu(locale_.old_peak_menu)

    SlpMenu = create_menu(locale_.slp_menu)
    CaaMenu = create_menu(locale_.caa_menu)

    ThallMenu = create_menu(locale_.thall_menu)

    #HideMenu = ReplyKeyboardMarkup(
    #    [
    #        [KeyboardButton(locale.HideMenu.HIDE_KEYBOARD)]
    #    ],
    #    resize_keyboard=True
    #)

    #Data1 = ReplyKeyboardMarkup(
    #    [KeyboardButton()]
    #)
