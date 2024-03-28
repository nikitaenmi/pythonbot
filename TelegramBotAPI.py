from telebot import types
import telebot
import webbrowser
from Database.DAL.BrandDAL import *
from key import key

bot = telebot.TeleBot (key)


@bot.message_handler(commands = ['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Посмотреть обувь")
    btn2 = types.KeyboardButton("Корзина")
    btn3 = types.KeyboardButton("Связаться с консультантом")
    btn4 = types.KeyboardButton("Настройки")
    btn5 = types.KeyboardButton("Ввести своё имя")
    markup.add(btn1,btn2,btn3, btn4,btn5)
    bot.send_message(message.chat.id, 'Привет!', reply_markup=markup)
    user_id = message.from_user.id
    if BrandDAL.search_brand(user_id) == True:
        bot.send_message(message.chat.id, "Ты в базе данных")
    else:
        bot.send_message(message.chat.id, "Ты не в базе")
        BrandDAL.new_brand(user_id)
        bot.send_message(message.chat.id, "Сохранил тебя")




@bot.message_handler(content_types=["text"])

def handle_text(message):

    if message.text == "Ввести своё имя":
        sent = bot.send_message(message.chat.id, "Введите своё имя:")
        bot.register_next_step_handler(sent,save_link)

    if message.text == "Посмотреть обувь":
        shoes_products(message)

    if message.text == "Корзина":
        basket(message)

    if message.text == "Настройки":
        settings(message)

    if message.text == 'Назад':
        start(message)

    if message.text == "Кроссовки №1":
        bot.send_message(message.chat.id, 'бархатные тяги')

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
    btn4 = types.KeyboardButton("Назад")
    markup.add(btn4)
    bot.send_message(message.chat.id,"Ваши кроссовки в корзине:", reply_markup=markup)

def settings(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Настройки №1")
    btn2 = types.KeyboardButton("Настройки №2")
    btn3 = types.KeyboardButton("Назад")
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, "Наши кроссовки:", reply_markup=markup)

bot.infinity_polling()