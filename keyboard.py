import telebot
import config

from telebot import types



startmarkup = types.InlineKeyboardMarkup()
tovar1 = types.InlineKeyboardButton(text = '🍪 14-17 лет', callback_data = 't1')
tovar2 = types.InlineKeyboardButton(text = '🍇 Студентки ', callback_data = 't2')
tovar3 = types.InlineKeyboardButton(text = '🍓 Вписка ', callback_data = 't3')
tovar4 = types.InlineKeyboardButton(text = '🍑 В школе ', callback_data = 't4')
tovar5 = types.InlineKeyboardButton(text = '🍒 Учитель и школьница ', callback_data = 't5')
tovar6 = types.InlineKeyboardButton(text = '🐱 Милфы ', callback_data = 't6')   
tovar7 = types.InlineKeyboardButton(text = '📣 Наш оператор', callback_data = 't7')

startmarkup.add(tovar1, tovar2, tovar3, tovar4, tovar5, tovar6, tovar7)