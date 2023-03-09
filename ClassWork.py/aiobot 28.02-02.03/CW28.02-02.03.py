import logging
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv, dotenv_values
import requests
 
load_dotenv()
config = dotenv_values(".env")
 
# Configure logging
logging.basicConfig(level=logging.INFO)
 
# Initialize bot and dispatcher
bot = Bot(token=config['API_TOKEN'])
dp = Dispatcher(bot)
 
@dp.message_handler(commands=['start', 's'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")
 
@dp.message_handler(commands=['help', 'h'])
async def send_help(message: types.Message):
    await message.reply("Hi!\nCan i help you?")
 
@dp.message_handler(commands=['cat', 'c'])
async def send_cat(message: types.Message):
    r = requests.get(config['LINK'])
    data = r.json()
    url = data[0]['url']
    await message.reply(url)
 
@dp.message_handler()
async def send_echo(message: types.Message):
    await bot.send_message(message.from_user.id, message.text)
 
 
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)