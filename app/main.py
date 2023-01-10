from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Text, Command
from aiogram.types.reply_keyboard import ReplyKeyboardRemove
from ml import Model
from database import DataBase

from state import BotStates
from config import TOKEN
from keyboards import Keyboards

storage = MemoryStorage()

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)
model = Model()
data_base = DataBase()


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
             '0 - Сахар меньший за 120мг/дл\n'
             '1 - Сахар більший за 120мг/дл\n'
             '-1 - Не знаю',
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
        text=f'Ваша відповідь: {fbs}'
    )

    await bot.send_message(
        chat_id=user.id,
        text='Оберіть ваш тип кардіограми:\n'
             'Значення 0: нормально\n'
             'Значення 1: наявність аномалії зубця ST-T (інверсії зубця T і/або елевація або депресія ST > 0,05 мВ)\n'
             'Значення 2: демонструє ймовірну або певну гіпертрофію лівого шлуночка за критеріями Естеса\n'
             'Значення -1: Не знаю',
        reply_markup=Keyboards.RestecgMenu
    )

    data_list.append(fbs)
    print(data_list)

    await BotStates.restecg_menu.set()


@dp.message_handler(content_types=['text'], state=[BotStates.restecg_menu])
async def restecg_message(message: types.Message):
    user = message.from_user

    restecg = int(message.text)

    await bot.send_message(
        chat_id=user.id,
        text=f'Ваша відповідь: {restecg}',
    )

    await bot.send_message(
        chat_id=user.id,
        text='Напишіть ваш максимальний пульс',
        reply_markup=Keyboards.ThalachhMenu
    )

    data_list.append(restecg)
    print(data_list)

    await BotStates.thalachh_menu.set()


@dp.message_handler(content_types=['text'], state=[BotStates.thalachh_menu])
async def thalachh_message(message: types.Message):
    user = message.from_user

    thalahh = int(message.text)

    await bot.send_message(
        chat_id=user.id,
        text=f'Ваша відповідь: {thalahh}',
    )

    await bot.send_message(
        chat_id=user.id,
        text='Чи є в вас стенокардія фізичного навантаження',
        reply_markup=Keyboards.ExngMenu
    )
    data_list.append(thalahh)
    print(data_list)

    await BotStates.exng_menu.set()


@dp.message_handler(content_types=['text'], state=[BotStates.exng_menu])
async def exng_message(message: types.Message):
    user = message.from_user

    exng = int(message.text)

    await bot.send_message(
        chat_id=user.id,
        text=f'Ваша відповідь: {exng}',
    )

    await bot.send_message(
        chat_id=user.id,
        text='Депресія ST, спричинена фізичним навантаженням, відносно відпочинку\n'
             ' \n'
             '(Десяткові дроби будь-ласка введіть через крапку)',
        reply_markup=Keyboards.OldpeakMenu
    )

    data_list.append(exng)
    print(data_list)

    await BotStates.oldpeak_menu.set()


@dp.message_handler(content_types=['text'], state=[BotStates.oldpeak_menu])
async def oldpeak_message(message: types.Message):
    user = message.from_user

    oldpeak = float(message.text)

    await bot.send_message(
        chat_id=user.id,
        text=f'Ваша відповідь: {oldpeak}',
    )

    await bot.send_message(
        chat_id=user.id,
        text='нахил піку навантаження сегмент ST — 0: спадний;\n'
             ' 1: плоский; 2: висхідний ',
        reply_markup=Keyboards.SlpMenu
    )

    data_list.append(oldpeak)
    print(data_list)

    await BotStates.caa_menu.set()


@dp.message_handler(content_types=['text'], state=[BotStates.caa_menu])
async def caa_message(message: types.Message):
    user = message.from_user

    caa = int(message.text)

    await bot.send_message(
        chat_id=user.id,
        text=f'Ваша відповідь: {caa}',
    )

    await bot.send_message(
        chat_id=user.id,
        text='number of major vessels\n'
             '0: , 1: , 2: , 3: .',
        reply_markup=Keyboards.SlpMenu
    )

    data_list.append(caa)
    print(data_list)

    await BotStates.slp_menu.set()


@dp.message_handler(content_types=['text'], state=[BotStates.slp_menu])
async def slp_message(message: types.Message):
    user = message.from_user

    slp = int(message.text)

    await bot.send_message(
        chat_id=user.id,
        text=f'Ваша відповідь: {slp}',
    )

    await bot.send_message(
        chat_id=user.id,
        text='Захворювання крові під назвою таласемія. Значення 0: НУЛЬ (вилучено з набору даних раніше\n'
             'Значення 1: фіксований дефект (відсутність кровотоку в деякій частині серця)\n'
             'Значення 2: нормальний кровотік'
             'Значення 3: оборотний дефект (потік крові спостерігається, але він не є нормальним)',
        reply_markup=Keyboards.ThallMenu
    )

    data_list.append(slp)
    print(data_list)

    await BotStates.thall_menu.set()


@dp.message_handler(content_types=['text'], state=[BotStates.thall_menu])
async def thall_message(message: types.Message):
    user = message.from_user
    thall = int(message.text)
    await bot.send_message(
        chat_id=user.id,
        text=f'Ваша відповідь: {thall}',
    )

    data_list.append(thall)
    print(data_list)

    print('HI')
    res = model.predict_proba([data_list])[0][1]
    await bot.send_message(
        chat_id=user.id,
        text=f'Ваша ризик: {res}\n'
             f'Відповідь може бути не точна якщо ви надали не достатьньо данних',
        reply_markup=Keyboards.MainMenu
    )

    await BotStates.main_menu.set()


@dp.message_handler(content_types=['text'], state=[BotStates.result])
async def result(message: types.Message):
    user = message.from_user
    print('HI')
    res = model.predict_proba([data_list])[0][1]
    await bot.send_message(
        chat_id=user.id,
        text=f'Ваша ризик: {res}\n'
             f'Відповідь може бути не точна якщо ви надали не достатьньо данних',
    )

    await bot.send_message(
        chat_id=user.id,
        text='Бажаєте щось ще?',
        reply_markup=Keyboards.MainMenu
    )
    print(res)
    await BotStates.main_menu.set()



@dp.message_handler(Text("Прочитати інструкцію"))
async def instruction_reply(message: types.Message):
    await message.reply("*інструкція*")


data_list = []
final_list = [data_list]

if __name__ == '__main__':
    executor.start_polling(dp)

#    await BotStates.main_menu.set()
