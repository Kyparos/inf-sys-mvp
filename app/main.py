from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Text, Command

from state import BotStates
from config import TOKEN
from keyboards import Keyboards

storage = MemoryStorage()

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands=['start'], state=[None])
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

    await BotStates.main_menu.set()


@dp.message_handler(Text("Надіслати дані"), state=[BotStates.main_menu])
async def interest_reply(message: types.Message):
    user = message.from_user

    await bot.send_message(
        chat_id=user.id,
        text='Надішліть свій вік'
        # reply_markup=Keyboards.HideMenu
    )

    # await BotStates.hide_menu.set()


@dp.message_handler(content_types=['text'], state=[BotStates.main_menu])
async def age_message(message: types.Message):
    user = message.from_user

    age = int(message.text)

    await bot.send_message(
        chat_id=user.id,
        text=f'Ваш вік {age}, а тепер надішліть пудласка стать',
    )

    await bot.send_message(
        chat_id=user.id,
        text=f'Оберіть вашу стать\n'
             f'0 - Чоловіча\n'
             f'1 - Жіноча',
        reply_markup=Keyboards.GenderMenu
    )
    data_list.append(age)
    print(data_list)

    await BotStates.gender_menu.set()


@dp.message_handler(content_types=['text'], state=BotStates.gender_menu)
async def gender_message(message: types.Message):
    user = message.from_user

    gender = int(message.text)

    await bot.send_message(
        chat_id=user.id,
        text=f'Ваша стать: {gender}'
    )

    await bot.send_message(
        chat_id=user.id,
        text='Опишіть свій біль',
        reply_markup=Keyboards.CpMenu
    )

    data_list.append(gender)
    print(data_list)

    await BotStates.cp_menu.set()


@dp.message_handler(content_types=['text'], state=BotStates.cp_menu)
async def cp_message(message: types.Message):
    user = message.from_user

    cp = int(message.text)

    await bot.send_message(
        chat_id=user.id,
        text=f'У вас {cp} вид болю'
    )

    await bot.send_message(
        chat_id=user.id,
        text='Напишіть свій кровяний тиск',
        reply_markup=Keyboards.TrtbpsMenu
    )

    await BotStates.trtbps_menu.set()

    data_list.append(cp)
    print(data_list)



@dp.message_handler(content_types=['text'], state=[BotStates.trtbps_menu])
async def trtbps_message(message: types.Message):
    user = message.from_user

    trtbps = int(message.text)

    await bot.send_message(
        chat_id=user.id,
        text=f'Ваш тиск: {trtbps}'
    )

    await bot.send_message(
        chat_id=user.id,
        text=f'Напишіть ваш рівень холестерину',
        reply_markup=Keyboards.CholMenu
    )

    await BotStates.chol_menu.set()

    data_list.append(trtbps)
    print(data_list)


@dp.message_handler(content_types=['text'], state=[BotStates.chol_menu])
async def chol_message(message: types.Message):
    user = message.from_user

    chol = int(message.text)

    await bot.send_message(
        chat_id=user.id,
        text=f'Ваш рівень холестерину: {chol}'
    )

    await bot.send_message(
        chat_id=user.id,
        text='Чи ваш рівень цукру більший за 120?\n'
             '1 - так\n'
             '0 - ні',
        reply_markup=Keyboards.FbsMenu
    )

    data_list.append(chol)
    print(data_list)

    await BotStates.fbs_menu.set()


@dp.message_handler(content_types=['text'], state=[BotStates.fbs_menu])
async def fbs_message(message: types.Message):
    user = message.from_user

    fbs = int(message.text)

    await bot.send_message(
        chat_id=user.id,
        text=f'Ваша відповідь: {fbs}',
    )

    await bot.send_message(
        chat_id=user.id,
        text='Оберіть ваш тип кардіограми:\n'
             '0 - \n'
             '1 - \n'
             '2 - \n'
             '-1 - ',
        reply_markup=Keyboards.RestecgMenu
    )

    data_list.append(fbs)
    print(data_list)

    await BotStates.restecg_menu.set()


@dp.message_handler(content_types=['text'], state=[BotStates.restecg_menu])
async def fbs_message(message: types.Message):
    user = message.from_user

    restecg = int(message.text)

    await bot.send_message(
        chat_id=user.id,
        text=f'Ваша відповідь: {restecg}',
    )

    await bot.send_message(
        chat_id=user.id,
        text='Напишіть ваш пульс',
        reply_markup=Keyboards.ThalachhMenu
    )

    data_list.append(restecg)
    print(data_list)

    await BotStates.thalachh_menu


@dp.message_handler(content_types=['text'], state=[BotStates.thalachh_menu])
async def fbs_message(message: types.Message):
    user = message.from_user

    restecg = int(message.text)

    await bot.send_message(
        chat_id=user.id,
        text=f'Ваша відповідь: {restecg}',
    )

    await bot.send_message(
        chat_id=user.id,
        text='Напишіть ваш пульс',
        reply_markup=Keyboards.ThalachhMenu
    )

    data_list.append(restecg)
    print(data_list)

    await BotStates.fbs_menu.set()


@dp.message_handler(Text("Прочитати інструкцію"))
async def instruction_reply(message: types.Message):
    await message.reply("*інструкція*")


data_list = []
final_list = [data_list]

if __name__ == '__main__':
    executor.start_polling(dp)

#    await BotStates.main_menu.set()
