import requests
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from setting import TOKEN

token = TOKEN
URL = 'https://cataas.com/cat'

bot = telebot.TeleBot(token)

keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(KeyboardButton('Получить котейку!'))


def get_cat():
    response = requests.get(URL)
    return response.content


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Чтобы получить котейку нажми кнопку "Получить котейку!"', reply_markup=keyboard)


@bot.message_handler(func=lambda s: 'кот' in s.text)
def cat_image_message(message):
    photo = get_cat()
    bot.send_photo(message.chat.id, photo)


print('Бот работает')
bot.infinity_polling()
