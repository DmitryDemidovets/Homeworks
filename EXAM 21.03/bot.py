import telebot
import requests
import datetime
import random
import sqlite3 
from telebot import types
from datetime import time


API_TOKEN = '6295259102:AAG4hcTklmlRwkC-s0e9WPBzq0N2-71hhuk'
bot = telebot.TeleBot(API_TOKEN)

#по команде /time показывает время
dt = datetime.datetime.now()
time = dt.time()
@bot.message_handler(commands= ['time'])
def send_time(message):
    bot.reply_to(message, str(time))

#по команде /sw показывает данные о разработчике
@bot.message_handler(commands= ['sw'])
def send_dev(message):
    bot.reply_to(message,'https://github.com/DmitryDemidovets')

#по команде /sticker присылает стикер
@bot.message_handler(commands=['sticker'])
def send_sticker(message):
    bot.send_sticker(message.chat.id,'CAACAgIAAxkBAAEIOTtkGfjbFBENhXTOlNjURgeQz67gOwAC_wIAAm2wQgMEoDmrNAI2Ny8E')


bot.infinity_polling()


 
