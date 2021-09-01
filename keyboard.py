import telebot
import config

from telebot import types



categories1 = types.InlineKeyboardMarkup()
  
categoriya2 = types.InlineKeyboardButton(text = '🦄 Категории', callback_data = 'buy')
categoriya3 = types.InlineKeyboardButton(text = '📣 Помощь', callback_data = 'categoriya2')
categories1.add(categoriya2, categoriya3)





categories = types.InlineKeyboardMarkup()
  
categoriya = types.InlineKeyboardButton(text = '🦄 Категории', callback_data = 'buy')
categoriya2 = types.InlineKeyboardButton(text = '📣 Помощь', callback_data = 'categoriya2')
categoriya3 = types.InlineKeyboardButton(text = '💭 Отзывы', callback_data = 'categoriya3')
categories.add(categoriya, categoriya2, categoriya3)



markup_inline1 = types.InlineKeyboardMarkup()
tovar1 = types.InlineKeyboardButton(text = '🍪 14-17 лет ', callback_data = 't1')
tovar2 = types.InlineKeyboardButton(text = '🍇 Студентки ', callback_data = 't2')
tovar3 = types.InlineKeyboardButton(text = '🍓 Вписка ', callback_data = 't3')
tovar4 = types.InlineKeyboardButton(text = '🍑 В школе ', callback_data = 't4')
tovar5 = types.InlineKeyboardButton(text = '🍒 Учитель и школьница ', callback_data = 't5')
tovar6 = types.InlineKeyboardButton(text = '🐱 Милфы ', callback_data = 't6')    

markup_inline1.add(tovar1, tovar5, tovar4, tovar3,tovar2, tovar6)
