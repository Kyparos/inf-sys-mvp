from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

import locale


class Keyboards:
    MainMenu = ReplyKeyboardMarkup(
        [
            [KeyboardButton(locale.MainMenu.INSTRUCTION)],
            [KeyboardButton(locale.MainMenu.REQUEST_DATA)]
        ],
        resize_keyboard=True
    )

    GenderMenu = ReplyKeyboardMarkup(
        [
            [KeyboardButton(locale.GenderMenu.MALE)],
            [KeyboardButton(locale.GenderMenu.FEMALE)]
        ],
        resize_keyboard=True
    )

    CpMenu = ReplyKeyboardMarkup(
        [
            [KeyboardButton(locale.CpMenu.PAIN1)],
            [KeyboardButton(locale.CpMenu.PAIN2)],
            [KeyboardButton(locale.CpMenu.PAIN3)],
            [KeyboardButton(locale.CpMenu.PAIN4)]
        ],
        resize_keyboard=True
    )

    HideMenu = ReplyKeyboardMarkup(
        [
            [KeyboardButton(locale.HideMenu.HIDE_KEYBOARD)]
        ],
        resize_keyboard=True
    )

    #Data1 = ReplyKeyboardMarkup(
    #    [KeyboardButton()]
    #)
