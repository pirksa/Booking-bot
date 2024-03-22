from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

buttons = [[KeyboardButton(text='Введите страну')],
           [KeyboardButton(text='Введите город')],
           [KeyboardButton(text='Введите здание')],
           [KeyboardButton(text='Введите компанию')],
           [KeyboardButton(text='Введите помещение')],
           [KeyboardButton(text='Введите бронирование')]
           ]
menu = ReplyKeyboardMarkup(keyboard=buttons, input_field_placeholder='Выберете действие', resize_keyboard=True)
