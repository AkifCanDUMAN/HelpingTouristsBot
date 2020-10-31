from main import dp, bot
from aiogram.types import Message, CallbackQuery
from config import admin_id
from default_keyboard import Country
from Inline_Keyboard import Images , AyasofyaCamii_URL , SultanAhmetCamii_URL
from Inline_Keyboard import Images2 , LaraDudenWaterfall_URL , HadrianCastleGate_URL
from Inline_Keyboard import Images3 ,IzmirClockTower_URL , IzmirHistoricalElevatorBuilding_URL
import logging

async def send_to_admin(dp):
    await bot.send_message(chat_id=admin_id,text='Bot is started')

@dp.message_handler()
async def speak(message: Message):
    if message.text.lower() == 'hello':
        await message.answer(f'Hello {message.from_user.first_name}')
    if message.text == '/help':
        await message.answer('some /Images function names and /Images ')
    if message.text == '/Country':
        await message.answer('choose a city', reply_markup=Country)
    if message.text == '/Images':
        await message.answer('Which city would you like to go to', reply_markup=Images)
    if message.text == '/Images2':
        await message.answer('Which city would you like to go to', reply_markup=Images2)
    if message.text == '/Images3':
        await message.answer('Which city would you like to go to', reply_markup=Images3)

@dp.callback_query_handler(text='AyasofyaMosque')
async def get_AyasofyaCamii(call: CallbackQuery):
    await call.answer(30)
    callback_data = call.data
    logging.info(f'call={callback_data}')

    await call.message.answer('You choise AyasofyaCamii', reply_markup=AyasofyaCamii_URL)

@dp.callback_query_handler(text='SultanAhmetMosque')
async def get_SultanAhmetCamii(call: CallbackQuery):
    await call.answer(30)
    callback_data = call.data
    logging.info(f'call={callback_data}')

    await call.message.answer('You choise SultanAhmetCamii', reply_markup=SultanAhmetCamii_URL)


@dp.callback_query_handler(text='LaraDudenWaterfall')
async def get_LaraDudenWaterfall(call: CallbackQuery):
    await call.answer(30)
    callback_data = call.data
    logging.info(f'call={callback_data}')

    await call.message.answer('You choise LaraDudenWaterfall', reply_markup=LaraDudenWaterfall_URL)

@dp.callback_query_handler(text='HadrianCastleGate')
async def get_HadrianCastleGate(call: CallbackQuery):
    await call.answer(30)
    callback_data = call.data
    logging.info(f'call={callback_data}')

    await call.message.answer('You choise HadrianCastleGate', reply_markup=HadrianCastleGate_URL)


@dp.callback_query_handler(text='IzmirClockTower')
async def get_IzmirClockTower(call: CallbackQuery):
    await call.answer(30)
    callback_data = call.data
    logging.info(f'call={callback_data}')

    await call.message.answer('You choise IzmirClockTower', reply_markup=IzmirClockTower_URL)

@dp.callback_query_handler(text='IzmirHistoricalElevatorBuilding')
async def get_IzmirHistoricalElevatorBuilding(call: CallbackQuery):
    await call.answer(30)
    callback_data = call.data
    logging.info(f'call={callback_data}')

    await call.message.answer('You choise IzmirHistoricalElevatorBuilding', reply_markup=IzmirHistoricalElevatorBuilding_URL)