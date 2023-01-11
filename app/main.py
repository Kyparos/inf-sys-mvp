from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Text, Command
from aiogram.types.reply_keyboard import ReplyKeyboardRemove
from ml import Model
from database import DataBase

from state import BotStates
from config import TOKEN
from keyboards import Keyboards
import locale_

def message_decode(val, dict_):
    return dict_.get(val, -1)


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
        text=f'Ваш вік {age}, а тепер надішліть будласка стать',
    )

    await bot.send_message(
        chat_id=user.id,
        text=f'Оберіть вашу стать',
        reply_markup=Keyboards.GenderMenu
    )
    data_list.append(age)
    print(data_list)

    await BotStates.gender_menu.set()


@dp.message_handler(content_types=['text'], state=BotStates.gender_menu)
async def gender_message(message: types.Message):
    user = message.from_user

    gender = message.text

    await bot.send_message(
        chat_id=user.id,
        text=f'Ваша стать: {gender}'
    )

    await bot.send_message(
        chat_id=user.id,
        text='Оценіть свій біль в груди від 0 до 3',
        reply_markup=Keyboards.CpMenu
    )

    data_list.append(message_decode(gender, locale_.gender_menu))
    print(data_list)

    await BotStates.cp_menu.set()


@dp.message_handler(content_types=['text'], state=BotStates.cp_menu)
async def cp_message(message: types.Message):
    user = message.from_user

    cp = message.text

    await bot.send_message(
        chat_id=user.id,
        text=f'У вас {cp}-й рівень болю'
    )

    await bot.send_message(
        chat_id=user.id,
        text='Напишіть свій кровяний тиск',
        reply_markup=Keyboards.TrtbpsMenu
    )

    await BotStates.trtbps_menu.set()

    data_list.append(message_decode(cp, locale_.cp_menu))
    print(data_list)


@dp.message_handler(content_types=['text'], state=[BotStates.trtbps_menu])
async def trtbps_message(message: types.Message):
    user = message.from_user

    trtbps = message.text

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
    trtbps = int(trtbps) if trtbps != locale_.DONT_KNOW else -1
    data_list.append(trtbps)
    print(data_list)


@dp.message_handler(content_types=['text'], state=[BotStates.chol_menu])
async def chol_message(message: types.Message):
    user = message.from_user

    chol = message.text

    await bot.send_message(
        chat_id=user.id,
        text=f'Ваш рівень холестерину: {chol}'
    )

    await bot.send_message(
        chat_id=user.id,
        text='Ваш рівень цукру ...',
        reply_markup=Keyboards.FbsMenu
    )
    chol = int(chol) if chol != locale_.DONT_KNOW else -1
    data_list.append(chol)
    print(data_list)

    await BotStates.fbs_menu.set()


@dp.message_handler(content_types=['text'], state=[BotStates.fbs_menu])
async def fbs_message(message: types.Message):
    user = message.from_user

    fbs = message.text

    await bot.send_message(
        chat_id=user.id,
        text=f'Ваша відповідь: {fbs}'
    )

    await bot.send_message(
        chat_id=user.id,
        text='Оберіть ваш тип кардіограми',
        reply_markup=Keyboards.RestecgMenu
    )

    data_list.append(message_decode(fbs, locale_.fbs_menu))
    print(data_list)

    await BotStates.restecg_menu.set()


@dp.message_handler(content_types=['text'], state=[BotStates.restecg_menu])
async def restecg_message(message: types.Message):
    user = message.from_user

    restecg = message.text

    await bot.send_message(
        chat_id=user.id,
        text=f'Ваша відповідь: {restecg}',
    )

    await bot.send_message(
        chat_id=user.id,
        text='Напишіть ваш максимальний пульс',
        reply_markup=Keyboards.ThalachhMenu
    )

    data_list.append(message_decode(restecg, locale_.restecg_menu))
    print(data_list)

    await BotStates.thalachh_menu.set()


@dp.message_handler(content_types=['text'], state=[BotStates.thalachh_menu])
async def thalachh_message(message: types.Message):
    user = message.from_user

    thalahh = message.text

    await bot.send_message(
        chat_id=user.id,
        text=f'Ваша відповідь: {thalahh}',
    )

    await bot.send_message(
        chat_id=user.id,
        text='Чи є в вас стенокардія фізичного навантаження',
        reply_markup=Keyboards.ExngMenu
    )
    thalahh = int(thalahh) if thalahh != locale_.DONT_KNOW else -1
    data_list.append(thalahh)
    print(data_list)

    await BotStates.exng_menu.set()


@dp.message_handler(content_types=['text'], state=[BotStates.exng_menu])
async def exng_message(message: types.Message):
    user = message.from_user

    exng = message.text

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

    data_list.append(message_decode(exng, locale_.exng_menu))
    print(data_list)

    await BotStates.oldpeak_menu.set()


@dp.message_handler(content_types=['text'], state=[BotStates.oldpeak_menu])
async def oldpeak_message(message: types.Message):
    user = message.from_user

    oldpeak = message.text

    await bot.send_message(
        chat_id=user.id,
        text=f'Ваша відповідь: {oldpeak}',
    )

    await bot.send_message(
        chat_id=user.id,
        text='КількістЬ звуженних головних артерій',
        reply_markup=Keyboards.SlpMenu
    )
    oldpeak = float(oldpeak) if oldpeak != locale_.DONT_KNOW else -1
    data_list.append(oldpeak)
    print(data_list)

    await BotStates.caa_menu.set()


@dp.message_handler(content_types=['text'], state=[BotStates.caa_menu])
async def caa_message(message: types.Message):
    user = message.from_user

    caa = message.text

    await bot.send_message(
        chat_id=user.id,
        text=f'Ваша відповідь: {caa}',
    )

    await bot.send_message(
        chat_id=user.id,
        text='нахил піку навантаження сегмент ST',
        reply_markup=Keyboards.CaaMenu
    )

    data_list.append(message_decode(caa, locale_.caa_menu))
    print(data_list)

    await BotStates.slp_menu.set()


@dp.message_handler(content_types=['text'], state=[BotStates.slp_menu])
async def slp_message(message: types.Message):
    user = message.from_user

    slp = message.text

    await bot.send_message(
        chat_id=user.id,
        text=f'Ваша відповідь: {slp}',
    )

    await bot.send_message(
        chat_id=user.id,
        text='Захворювання крові під назвою таласемія',
        reply_markup=Keyboards.ThallMenu
    )

    data_list.append(message_decode(slp, locale_.slp_menu))
    print(data_list)

    await BotStates.thall_menu.set()


@dp.message_handler(content_types=['text'], state=[BotStates.thall_menu])
async def thall_message(message: types.Message):
    user = message.from_user
    thall = message.text
    await bot.send_message(
        chat_id=user.id,
        text=f'Ваша відповідь: {thall}',
    )

    data_list.append(message_decode(thall, locale_.thall_menu))
    print(data_list)

    print('HI')
    res = model.predict_proba([data_list])[0][1]
    await bot.send_message(
        chat_id=user.id,
        text=f'Ваша ризик: {res:.2%}\n'
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
        text=f'Ваша ризик: {res:.2%}\n'
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
