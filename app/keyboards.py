from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

import locale

class Keyboards:

    MainMenu = ReplyKeyboardMarkup(
        [
            [KeyboardButton(locale.MainMenu.INSTRUCTION)]
        ]
    )