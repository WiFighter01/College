import requests
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from settingstoken import TOKEN

token = TOKEN
URL = 'https://cataas.com/cat'

bot = telebot.TeleBot(token)

keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(KeyboardButton('Hello'))
keyboard.add(KeyboardButton('Bye'))
keyboard.add(KeyboardButton('Получить котейку!'))


def get_cat():
    response = requests.get(URL)
    return response.content


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Ну привет!', reply_markup=keyboard)


@bot.message_handler(regexp=r'hello\.*')
def say_hello(message):
    bot.send_message(message.chat.id, 'Hello!')


@bot.message_handler(func=lambda s: 'Bye' in s.text)
def echo_message(message):
    bot.send_message(message.chat.id, 'Bye!')


@bot.message_handler(func=lambda s: 'кот' in s.text)
def cat_image_message(message):
    photo = get_cat()
    bot.send_photo(message.chat.id, photo)
    # gif send_video
    # dog.ceo/dog-api/


# @bot.message_handler(content_types=['text'])
# def echo_message(message):
#     bot.send_message(message.chat.id, message.text)


print('Бот работает')
bot.infinity_polling()
