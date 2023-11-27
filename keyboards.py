from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

buttons = [[KeyboardButton(text='Введите страну')],
           [KeyboardButton(text='Введите город')]
           ]
menu = ReplyKeyboardMarkup(keyboard=buttons, input_field_placeholder='Выберете действие', resize_keyboard=True)
