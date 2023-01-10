from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

import locale_


class Keyboards:
    MainMenu = ReplyKeyboardMarkup(
        [
            [KeyboardButton(locale_.MainMenu.INSTRUCTION)],
            [KeyboardButton(locale_.MainMenu.REQUEST_DATA)]
        ],
        resize_keyboard=True
    )

    GenderMenu = ReplyKeyboardMarkup(
        [
            [KeyboardButton(locale_.GenderMenu.MALE)],
            [KeyboardButton(locale_.GenderMenu.FEMALE)]
        ],
        resize_keyboard=True
    )

    CpMenu = ReplyKeyboardMarkup(
        [
            [KeyboardButton(locale_.CpMenu.PAIN1)],
            [KeyboardButton(locale_.CpMenu.PAIN2)],
            [KeyboardButton(locale_.CpMenu.PAIN3)],
            [KeyboardButton(locale_.CpMenu.PAIN0)]
        ],
        resize_keyboard=True
    )

    TrtbpsMenu = ReplyKeyboardMarkup(
        [
            [KeyboardButton(locale_.TrtbpsMenu.DONTKNOW)]
        ]
    )

    CholMenu = ReplyKeyboardMarkup(
        [
            [KeyboardButton(locale_.CholMenu.DONTKNOW)]
        ]
    )


    FbsMenu = ReplyKeyboardMarkup(
        [
            [KeyboardButton(locale_.FbsMenu.MORE120)],
            [KeyboardButton(locale_.FbsMenu.LESS120)],
            [KeyboardButton(locale_.FbsMenu.DONTKNOW)]
        ]
    )


    RestecgMenu = ReplyKeyboardMarkup(
        [
            [KeyboardButton(locale_.RestecgMenu.RESULT0)],
            [KeyboardButton(locale_.RestecgMenu.RESULT1)],
            [KeyboardButton(locale_.RestecgMenu.RESULT2)],
            [KeyboardButton(locale_.RestecgMenu.DONTKNOW)]
        ]
    )

    ThalachhMenu = ReplyKeyboardMarkup(
        [
            [KeyboardButton(locale_.ThalachhMenu.DONTKNOW)]
        ]
    )

    ExngMenu = ReplyKeyboardMarkup(
        [
            [KeyboardButton(locale_.ExngMenu.RESULT0)],
            [KeyboardButton(locale_.ExngMenu.RESULT1)],
            [KeyboardButton(locale_.ExngMenu.DONTKNOW)]

        ]
    )

    OldpeakMenu = ReplyKeyboardMarkup(
        [
            [KeyboardButton(locale_.OldpeakMenu.DONTKNOW)]
        ]
    )

    SlpMenu = ReplyKeyboardMarkup(
        [
            [KeyboardButton(locale_.SlpMenu.RESULT0)],
            [KeyboardButton(locale_.SlpMenu.RESULT1)],
            [KeyboardButton(locale_.SlpMenu.RESULT2)],
            [KeyboardButton(locale_.SlpMenu.DONTKNOW)]
        ]
    )

    CaaMenu = ReplyKeyboardMarkup(
        [
            [KeyboardButton(locale_.CaaMenu.RESULT0)],
            [KeyboardButton(locale_.CaaMenu.RESULT1)],
            [KeyboardButton(locale_.CaaMenu.RESULT2)],
            [KeyboardButton(locale_.CaaMenu.RESULT3)],
            [KeyboardButton(locale_.CaaMenu.DONTKNOW)]

        ]
    )

    ThallMenu = ReplyKeyboardMarkup(
        [
            [KeyboardButton(locale_.ThallMenu.RESULT1)],
            [KeyboardButton(locale_.ThallMenu.RESULT2)],
            [KeyboardButton(locale_.ThallMenu.RESULT3)],
            [KeyboardButton(locale_.ThallMenu.DONTKNOW)]

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
