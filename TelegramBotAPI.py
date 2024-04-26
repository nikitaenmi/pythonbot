from telebot import types
import telebot
import webbrowser
from Database.DAL.BrandDAL import *
from key import key

bot = telebot.TeleBot (key)


@bot.message_handler(commands = ['start'])
def start(message):
    keyboard = types.InlineKeyboardMarkup()
    a1 = types.InlineKeyboardButton(text="Посмотреть обувь", callback_data="shoesView")
    a2 = types.InlineKeyboardButton(text="Корзина", callback_data="a2")
    a3 = types.InlineKeyboardButton(text="Связаться с консультантом", callback_data="a3")
    a4 = types.InlineKeyboardButton(text="Настройки", callback_data="a4")
    a5 = types.InlineKeyboardButton(text="Ввести своё имя", callback_data="a5")
    a6 = types.InlineKeyboardButton(text="Назад", callback_data="a6")
    keyboard.add(a1, a2, a3, a4, a5, a6)
    bot.send_message(message.chat.id, 'Здравствуйте', reply_markup=keyboard)

    user_id = message.from_user.id
    if BrandDAL.search_brand(user_id) == True:
        bot.send_message(message.chat.id, "Ты в базе данных")
    else:
        bot.send_message(message.chat.id, "Ты не в базе")
        BrandDAL.new_brand(user_id)
        bot.send_message(message.chat.id, "Сохранил тебя")

    # markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # btn1 = types.KeyboardButton("Посмотреть обувь")
    # btn2 = types.KeyboardButton("Корзина")
    # btn3 = types.KeyboardButton("Связаться с консультантом")
    # btn4 = types.KeyboardButton("Настройки")
    # btn5 = types.KeyboardButton("Ввести своё имя")
    # markup.add(btn1,btn2,btn3, btn4,btn5)
    # bot.send_message(message.chat.id, 'Привет!', reply_markup=markup)
    # user_id = message.from_user.id
    # if BrandDAL.search_brand(user_id) == True:
    #     bot.send_message(message.chat.id, "Ты в базе данных")
    # else:
    #     bot.send_message(message.chat.id, "Ты не в базе")
    #     BrandDAL.new_brand(user_id)
    #     bot.send_message(message.chat.id, "Сохранил тебя")




@bot.message_handler(content_types=["text"])

def handle_text(message):

    if message.text == "Очистить корзину":
        BrandDAL.delete_basket(message.from_user.id)
        bot.send_message(message.chat.id, "Корзина очищена!")

    if message.text == "Ввести своё имя":
        sent = bot.send_message(message.chat.id, "Введите своё имя:")
        bot.register_next_step_handler(sent,save_link)

    if message.text == "Посмотреть обувь":
        shoes_products(message)

    if message.text == "Корзина":
        basket(message)
        bot.send_message(message.chat.id, str(BrandDAL.search_basket(message.from_user.id)))


    if message.text == "Настройки":
        settings(message)

    if message.text == 'Назад':
        start(message)

    if message.text == "Кроссовки №1":
        sneakers(message)
        #bot.send_message(message.chat.id, 'бархатные тяги')

    if message.text == "Кроссовки №2":
        pass


    if message.text == 'Добавить в корзину кросоовки №1':
        keyboard = types.InlineKeyboardMarkup()
        b1 = types.InlineKeyboardButton(text="41", callback_data="b1")
        b2 = types.InlineKeyboardButton(text="42", callback_data="b2")
        b3 = types.InlineKeyboardButton(text="43", callback_data="b3")
        b4 = types.InlineKeyboardButton(text="44", callback_data="b4")
        b5 = types.InlineKeyboardButton(text="45", callback_data="b5")
        b6 = types.InlineKeyboardButton(text="Назад", callback_data="b6")
        keyboard.add(b1,b2,b3,b4,b5,b6)
        bot.send_message(message.chat.id, 'Выберите размер:', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == "shoesView":
            keyboard = types.InlineKeyboardMarkup()
            b1 = types.InlineKeyboardButton(text="Кроссовки №1", callback_data="sneakerFirst")
            b2 = types.InlineKeyboardButton(text="Кроссовки №2", callback_data="sneakerSecond")
            b3 = types.InlineKeyboardButton(text="Кроссовки №3", callback_data="sneakerThirth")
            b4 = types.InlineKeyboardButton(text="Назад", callback_data="backStore")

            keyboard.add(b1, b2, b3, b4)
            bot.send_message(call.message.chat.id, 'Наши кроссовки:', reply_markup=keyboard)

        if call.data == "backStore":
            start(call.message)

        if call.data == "sneakerFirst":
            keyboard = types.InlineKeyboardMarkup()
            b1 = types.InlineKeyboardButton(text="Добавить в корзину", callback_data="sneakerAdd")
            b2 = types.InlineKeyboardButton(text="Назад", callback_data="sneakerBack")
            keyboard.add(b1,b2)
            bot.send_message(call.message.chat.id, "Кроссовки №1", reply_markup=keyboard)

        if call.data  == "sneakerBack":
            start(call.message)

        if call.data == "sneakerAdd":
            keyboard = types.InlineKeyboardMarkup()
            b1 = types.InlineKeyboardButton(text="41", callback_data="b1")
            b2 = types.InlineKeyboardButton(text="42", callback_data="b2")
            b3 = types.InlineKeyboardButton(text="43", callback_data="b3")
            b4 = types.InlineKeyboardButton(text="44", callback_data="b4")
            b5 = types.InlineKeyboardButton(text="45", callback_data="b5")
            b6 = types.InlineKeyboardButton(text="Назад", callback_data="b6")
            keyboard.add(b1, b2, b3, b4, b5, b6)
            bot.send_message(call.message.chat.id, 'Выберите размер:', reply_markup=keyboard)


















        if call.data == "b1":
            bot.send_message(call.message.chat.id, "Вы нажали на первую кнопку.")

        if call.data == "b2":
            bot.send_message(call.message.chat.id, "Вы нажали на вторую кнопку.")
        if call.data == "b3":
            bot.send_message(call.message.chat.id, "Вы нажали на вторую кнопку.")
        if call.data == "b4":
            bot.send_message(call.message.chat.id, "Вы нажали на вторую кнопку.")
        if call.data == "b5":
            bot.send_message(call.message.chat.id, "Вы нажали на вторую кнопку.")
        if call.data == "b6":
            start(message)


       # if message.text == "43":
           # id = message.from_user.id
         #   BrandDAL.add_basket('Бархатные тяги', id)

    #if message.text == "Добавить в корзину":


def save_link(message):
   my_link = message.text
   BrandDAL.new_brand(my_link)
   bot.send_message(message.chat.id, "Сохранил!")
   start(message)


def username(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn2 = types.KeyboardButton("Выйти")
    btn3 = types.KeyboardButton("Посмотреть обувь")
    markup.add(btn2, btn3)
    bot.send_message(message.chat.id, 'Имя успешно задано!',reply_markup=markup)

def shoes_products(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Кроссовки №1")
    btn2 = types.KeyboardButton("Кроссовки №2")
    btn3 = types.KeyboardButton("Кроссовки №3")
    btn4 = types.KeyboardButton("Назад")
    markup.add(btn1, btn2, btn3, btn4)
    bot.send_message(message.chat.id,"Наши кроссовки:", reply_markup=markup)




def basket(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn3= types.KeyboardButton("Очистить корзину")
    btn4 = types.KeyboardButton("Назад")
    markup.add(btn3,btn4)
    bot.send_message(message.chat.id,"Ваши кроссовки в корзине:", reply_markup=markup)

def settings(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Настройки №1")
    btn2 = types.KeyboardButton("Настройки №2")
    btn3 = types.KeyboardButton("Назад")
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, "Наши кроссовки:", reply_markup=markup)


def sneakers(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Добавить в корзину кросоовки №1")
    btn2 = types.KeyboardButton("Назад")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, "Бархатные тяги", reply_markup=markup)

bot.infinity_polling()