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

    FbsMenu = ReplyKeyboardMarkup(
        [
            [KeyboardButton(locale.FbsMenu.MORE120)],
            [KeyboardButton(locale.FbsMenu.LESS120)]
        ]
    )

    TrtbpsMenu = ReplyKeyboardMarkup(
        [
            [KeyboardButton(locale.TrtbpsMenu.DONTKNOW)]
        ]
    )

    CholMenu = ReplyKeyboardMarkup(
        [
            [KeyboardButton(locale.CholMenu.DONTKNOW)]
        ]
    )

    Restecg = ReplyKeyboardMarkup(
        [
            [KeyboardButton(locale.]
            [KeyboardButton(locale.]
            [KeyboardButton(locale.]

        ]
    )

    #HideMenu = ReplyKeyboardMarkup(
    #    [
    #        [KeyboardButton(locale.HideMenu.HIDE_KEYBOARD)]
    #    ],
    #    resize_keyboard=True
    #)

    #Data1 = ReplyKeyboardMarkup(
    #    [KeyboardButton()]
    #)
