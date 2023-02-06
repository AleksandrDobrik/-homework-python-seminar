from aiogram import  types
from create import dp
from aiogram.dispatcher.filters import Text
from random import randint as RI
from datetime import datetime
 
total = 150
pve_dict = dict()



@dp.message_handler(commands=['help'])
async def mes_help(message: types.Message):
    await message.answer('Пока я еще ничего не умеюб но обязательно научусь')


@dp.message_handler(commands=['hi'])
async def mes_start(message: types.Message):
    await message.answer(f'Привет {message.from_user.first_name}! Мы будем играть с тобой в конфетки')

@dp.message_handler(commands=['start'])
async def mes_start(message: types.Message):
    global total
    global pve_dict
    await message.answer(f'{message.from_user.first_name}!'
                                'На стол кладется некоторое количество конфет.\n'
                                'Мы с тобой по-очереди берём со стола произвольное количество конфет, '
                                'но не менее одной и не более двадцати восьми.\n'
                                'Победит тот кто заберёт со стола последние конфеты!\n\n'
                                'И так на столе 150 конфет твой ход.\n'
                                )
    user = []  
    user .append(message.from_user.full_name)
    user .append(message.from_user.username)
    user .append(message.from_user.id)
    user .append(datetime.now())
    user = list(map( str, user))
    with open('text.txt', 'a', encoding='UTF-8') as data:
        data.write(':'.join(user)+ '\n')


    user_id = message.from_user.id
    pve_dict[user_id] = total
    print((pve_dict))

    
@dp.message_handler()
async def mes_all(message: types.Message):
    global total
    global pve_dict
    if message.text.isdigit():
        user_id_message = message.from_user.id
        candy_left = pve_dict[user_id_message]
        candy_left -= int(message.text)
        await message.answer(f'На столе осталось {candy_left} конфет')
        if candy_left <= 0:
            await message.answer(f'Вы победили!')
            pve_dict[user_id]  = total
        else:
            hod_bot = candy_left % 29
            if hod_bot == 0:
                hod_bot = RI(1,28)
            await message.answer(f'А я заберу {hod_bot} конфет')
            candy_left -= hod_bot
            await message.answer(f'На столе осталось {candy_left} конфет')
            if candy_left <= 0:
                pve_dict[user_id]  = total
                await message.answer(f'Победил бот!')
            else:
                pve_dict[user_id_message] = candy_left



