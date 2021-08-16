# -*- coding: utf-8 -*-
import telebot
import config
import keyboard
from telebot import types

bot = telebot.TeleBot(config.TOKEN)




@bot.message_handler(commands=['start'])
def start(message):
    markup_inline = types.InlineKeyboardMarkup()
    tovar1 = types.InlineKeyboardButton(text = '🍪 14-17 лет ', callback_data = 't1')
    tovar2 = types.InlineKeyboardButton(text = '🍇 Студентки ', callback_data = 't2')
    tovar3 = types.InlineKeyboardButton(text = '🍓 Вписка ', callback_data = 't3')
    tovar4 = types.InlineKeyboardButton(text = '🍑 В школе ', callback_data = 't4')
    tovar5 = types.InlineKeyboardButton(text = '🍒 Учитель и школьница ', callback_data = 't5')
    tovar6 = types.InlineKeyboardButton(text = '🐱 Милфы ', callback_data = 't6')    
    tovar7 = types.InlineKeyboardButton(text = '📣 Помощь', callback_data = 't7')

    markup_inline.add(tovar1, tovar5, tovar4, tovar3,tovar2, tovar6, tovar7)

    photo = open("welcome/hello.jpg", 'rb')
    bot.send_photo(message.chat.id, photo, caption='🔥 <b>Добро пожаловать в наш магазин, ты попал по адресу!</b>\n\n<i>💞 Спасибо, что используешь нашего бота!</i>\n👇 <i>Что-бы использовать бота, используй кнопки снизу.</i>', reply_markup = markup_inline, parse_mode = 'html')
 


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == 't1':
            markup_inline = types.InlineKeyboardMarkup()
            variant1 = types.InlineKeyboardButton(text = '✅ Я оплатил', callback_data = 'oplata')
            variant2 = types.InlineKeyboardButton(text = '🔙 В главное меню', callback_data = 'back')

            markup_inline.add(variant1, variant2)
            idd = call.message.from_user.id
            bot.send_message(call.message.chat.id, f'➖➖➖➖➖➖➖➖➖➖\n<b>Вы выбрали:</b>🍪 <i>Школьницы 14-17 лет\n<b>Описание:</b> <i>20 фото + 30 видео</i></i>\n➖➖➖➖➖➖➖➖➖➖\n🥝 <b>Оплата через QIWI:</b>\n<b>❗️ Цена:</b> <i>99₽</i>\n<b>💰 QIWI кошелёк для оплаты:</b> <i>+79601599809</i>\n<b>💭 Комментарий к переводу:</b> <i>{idd}</i>\n\n➖➖➖➖➖➖➖➖➖➖\n\n<b>💳 Оплата картой:</b>\n\n<b>Номер карты для перевода:</b> <i>4890 4947 3644 2443</i>\n<code>[Переводить ровно указанную сумму, комиссия никак не повлияет!]</code>', reply_markup=markup_inline, parse_mode='html')



        if call.data == 'back':
            bot.send_message(call.message.chat.id, '❗️ Вы вернулись назад!\n\n🔥 <b>Добро пожаловать в наш магазин, ты попал по адресу!</b>\n\n<i>💞 Спасибо, что используешь нашего бота!</i>\n👇 <i>Что-бы использовать бота, используй кнопки снизу.</i>', reply_markup=keyboard.startmarkup, parse_mode='html')



        if call.data == 'oplata':
            bot.send_message(call.message.chat.id, '❕ Оплата не найдена. Попробуйте ещё раз через 10-20 секунд.')



        if call.data == 't2':
            markup_inline = types.InlineKeyboardMarkup()
            variant1 = types.InlineKeyboardButton(text = '✅ Я оплатил', callback_data = 'oplata')
            variant2 = types.InlineKeyboardButton(text = '🔙 В главное меню', callback_data = 'back')

            markup_inline.add(variant1, variant2)
            idd = call.message.from_user.id
            bot.send_message(call.message.chat.id, f'➖➖➖➖➖➖➖➖➖➖\n<b>Вы выбрали:</b>🍇 <i>Студентки\n<b>Описание:</b> <i>15 фото + 50 видео</i></i>\n➖➖➖➖➖➖➖➖➖➖\n🥝 <b>Оплата через QIWI:</b>\n<b>❗️ Цена:</b> <i>129₽</i>\n<b>💰 QIWI кошелёк для оплаты:</b> <i>+79601599809</i>\n<b>💭 Комментарий к переводу:</b> <i>{idd}</i>\n\n➖➖➖➖➖➖➖➖➖➖\n\n<b>💳 Оплата картой:</b>\n\n<b>Номер карты для перевода:</b> <i>4890 4947 3644 2443</i>\n<code>[Переводить ровно указанную сумму, комиссия никак не повлияет!]</code>', reply_markup=markup_inline, parse_mode='html')


        if call.data == 't3':
            markup_inline = types.InlineKeyboardMarkup()
            variant1 = types.InlineKeyboardButton(text = '✅ Я оплатил', callback_data = 'oplata')
            variant2 = types.InlineKeyboardButton(text = '🔙 В главное меню', callback_data = 'back')

            markup_inline.add(variant1, variant2)
            idd = call.message.from_user.id
            bot.send_message(call.message.chat.id, f'➖➖➖➖➖➖➖➖➖➖\n<b>Вы выбрали:</b>🍓 <i>Вписка школьников\n<b>Описание:</b> <i>1 видео длительностью 15 минут</i></i>\n➖➖➖➖➖➖➖➖➖➖\n🥝 <b>Оплата через QIWI:</b>\n<b>❗️ Цена:</b> <i>49₽</i>\n<b>💰 QIWI кошелёк для оплаты:</b> <i>+79601599809</i>\n<b>💭 Комментарий к переводу:</b> <i>{idd}</i>\n\n➖➖➖➖➖➖➖➖➖➖\n\n<b>💳 Оплата картой:</b>\n\n<b>Номер карты для перевода:</b> <i>4890 4947 3644 2443</i>\n<code>[Переводить ровно указанную сумму, комиссия никак не повлияет!]</code>', reply_markup=markup_inline, parse_mode='html')


        if call.data == 't4':
            markup_inline = types.InlineKeyboardMarkup()
            variant1 = types.InlineKeyboardButton(text = '✅ Я оплатил', callback_data = 'oplata')
            variant2 = types.InlineKeyboardButton(text = '🔙 В главное меню', callback_data = 'back')

            markup_inline.add(variant1, variant2)
            idd = call.message.from_user.id
            bot.send_message(call.message.chat.id, f'➖➖➖➖➖➖➖➖➖➖\n<b>Вы выбрали:</b>🍑 <i>Прямо в школе\n<b>Описание:</b> <i>3 видео, каждое длительностью ~5 минут. Минет и секс в туалете.</i></i>\n➖➖➖➖➖➖➖➖➖➖\n🥝 <b>Оплата через QIWI:</b>\n<b>❗️ Цена:</b> <i>199₽</i>\n<b>💰 QIWI кошелёк для оплаты:</b> <i>+79601599809</i>\n<b>💭 Комментарий к переводу:</b> <i>{idd}</i>\n\n➖➖➖➖➖➖➖➖➖➖\n\n<b>💳 Оплата картой:</b>\n\n<b>Номер карты для перевода:</b> <i>4890 4947 3644 2443</i>\n<code>[Переводить ровно указанную сумму, комиссия никак не повлияет!]</code>', reply_markup=markup_inline, parse_mode='html')


        if call.data == 't5':
            markup_inline = types.InlineKeyboardMarkup()
            variant1 = types.InlineKeyboardButton(text = '✅ Я оплатил', callback_data = 'oplata')
            variant2 = types.InlineKeyboardButton(text = '🔙 В главное меню', callback_data = 'back')

            markup_inline.add(variant1, variant2)
            idd = call.message.from_user.id
            bot.send_message(call.message.chat.id, f'➖➖➖➖➖➖➖➖➖➖\n<b>Вы выбрали:</b>🍒 <i>Учитель и школьница(по настоящему)\n<b>Описание:</b> <i>2 видео. Длительность 5-10 минут, только минет.</i></i>\n➖➖➖➖➖➖➖➖➖➖\n🥝 <b>Оплата через QIWI:</b>\n<b>❗️ Цена:</b> <i>99₽</i>\n<b>💰 QIWI кошелёк для оплаты:</b> <i>+79601599809</i>\n<b>💭 Комментарий к переводу:</b> <i>{idd}</i>\n\n➖➖➖➖➖➖➖➖➖➖\n\n<b>💳 Оплата картой:</b>\n\n<b>Номер карты для перевода:</b> <i>4890 4947 3644 2443</i>\n<code>[Переводить ровно указанную сумму, комиссия никак не повлияет!]</code>', reply_markup=markup_inline, parse_mode='html')

        if call.data == 't7':
            markup_inline = types.InlineKeyboardMarkup() 
            variant1 = types.InlineKeyboardButton(text = '✅ Оператор', url = 'https://t.me/LoliSh0p')            
            variant2 = types.InlineKeyboardButton(text = '🔙 В главное меню', callback_data = 'back')
            markup_inline.add(variant2, variant1)
            bot.send_message(call.message.chat.id, '<b>FAQ:</b>\n\n<b>Как мне купить товар?</b>\n-<i> Вы выбираете интересующий вас товар, после чего вы можете оплатить его с помощью QIWI или переводом на карту. Переводить нужно точно указанную сумму, в ином случае платёж не засчитается. После перевода средств, вы нажимаете на кнопку "Я оплатил", и в течении 5 секунд бот выдаст ваш товар.</i>\n\n<b>Что делать в случае, если бот не выдал товар?</b>\n<i>- Скорей всего, вы не указали комментарий при переводе на киви, или в случае с картой, ввели не точно указанную сумму. Вы можете обратиться к нашему оператору, что бы он самостоятельно выдал ваш товар.</i>\n\n<b>Безопасно ли это?</b>\n<i>- Покупка происходит через автоматического бота, ваши данные полностью защищены. Мы не видим ваших данных, деньги приходят нам на BTC кошелек.</i>\n\n<b>На этом всё, по остальным вопросам обращаться к нашему модератору (кнопка есть снизу).</b>', parse_mode='html', reply_markup=markup_inline)



        if call.data == 't6':
            markup_inline = types.InlineKeyboardMarkup()
            variant1 = types.InlineKeyboardButton(text = '✅ Я оплатил', callback_data = 'oplata')
            variant2 = types.InlineKeyboardButton(text = '🔙 В главное меню', callback_data = 'back')

            markup_inline.add(variant1, variant2)
            idd = call.message.from_user.id
            bot.send_message(call.message.chat.id, f'➖➖➖➖➖➖➖➖➖➖\n<b>Вы выбрали:</b>🐱 <i>Милфы\n<b>Описание:</b> <i>Огромный пак с милфами с PornHub PREMIUM аккаунта.</i></i>\n➖➖➖➖➖➖➖➖➖➖\n🥝 <b>Оплата через QIWI:</b>\n<b>❗️ Цена:</b> <i>129₽</i>\n<b>💰 QIWI кошелёк для оплаты:</b> <i>+79601599809</i>\n<b>💭 Комментарий к переводу:</b> <i>{idd}</i>\n\n➖➖➖➖➖➖➖➖➖➖\n\n<b>💳 Оплата картой:</b>\n\n<b>Номер карты для перевода:</b> <i>4890 4947 3644 2443</i>\n<code>[Переводить ровно указанную сумму, комиссия никак не повлияет!]</code>', reply_markup=markup_inline, parse_mode='html')


bot.polling(none_stop=True)
