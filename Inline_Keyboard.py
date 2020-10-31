from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import AyasofyaCamiiurlsi
from config import SultanAhmetCamiiurlsi
from config import LaraDudenWaterfallurlsi
from config import HadrianCastleGateurlsi
from config import IzmirClockTowerurlsi
from config import IzmirHistoricalElevatorBuildingurlsi


Images = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='AyasofyaCamii', callback_data='AyasofyaMosque'),
            InlineKeyboardButton(text='SultanAhmetCamii', callback_data='SultanAhmetMosque')
        ],
        [
            InlineKeyboardButton(text='Geri', callback_data='cancel')
        ]
    ],

)
AyasofyaCamii_URL= InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='To GO', url=AyasofyaCamiiurlsi),
            InlineKeyboardButton(text='Vazgeç', callback_data='cancel')
        ]
    ]
)
SultanAhmetCamii_URL= InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='To Go', url=SultanAhmetCamiiurlsi),
            InlineKeyboardButton(text='Vazgeç', callback_data='cancel')
        ]
    ]
)
Images2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='LaraDüdenWaterfall', callback_data='LaraDüdenWaterfall'),
            InlineKeyboardButton(text='HadrianCastleGate', callback_data='HadrianCastleGate')
        ],
        [
            InlineKeyboardButton(text='Geri', callback_data='cancel')
        ]
    ],

)
LaraDudenWaterfall_URL= InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='To GO', url=LaraDudenWaterfallurlsi),
            InlineKeyboardButton(text='Vazgeç', callback_data='cancel')
        ]
    ]
)
HadrianCastleGate_URL= InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='To Go', url=HadrianCastleGateurlsi),
            InlineKeyboardButton(text='Vazgeç', callback_data='cancel')
        ]
    ]
)
Images3 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='IzmirClockTower', callback_data='IzmirClockTower'),
            InlineKeyboardButton(text='IzmirHistoricalElevatorBuilding', callback_data='IzmirHistoricalElevatorBuilding')
        ],
        [
            InlineKeyboardButton(text='Geri', callback_data='cancel')
        ]
    ],

)
IzmirClockTower_URL= InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='To GO', url=IzmirClockTowerurlsi),
            InlineKeyboardButton(text='Vazgeç', callback_data='cancel')
        ]
    ]
)
IzmirHistoricalElevatorBuilding_URL= InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='To Go', url=IzmirHistoricalElevatorBuildingurlsi),
            InlineKeyboardButton(text='Vazgeç', callback_data='cancel')
        ]
    ]
)