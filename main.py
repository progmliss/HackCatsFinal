import telebot
import random
from telebot import types

bot = telebot.TeleBot('6498841174:AAEyIPJd1vrKWG4f3_2cSWyjeR-IhfJUuM8')

@bot.message_handler(command=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Введите ФИО: ')
    name = message.text
    user_id = random.randint(100000, 999999)

bot.polling(none_stop=True)