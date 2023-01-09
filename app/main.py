from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Text, Command

#from state import BotStates
from config import TOKEN
from keyboards import Keyboards

storage = MemoryStorage()

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    user = message.from_user

    await bot.send_message(
        chat_id=user.id,
        text=f'Вітаю, {user.first_name}'
    )

    await bot.send_message(
        chat_id=user.id,
        text='Що саме Вас цікавить?',
        reply_markup=Keyboards.MainMenu
    )



if __name__ == '__main__':
    executor.start_polling(dp)

#    await BotStates.main_menu.set()
