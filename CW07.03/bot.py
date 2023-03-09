import logging
from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
 
 
logging.basicConfig(level=logging.INFO)
 
API_TOKEN = '5903970547:AAEM8noQV5yi2Ij4mA351NFu9ArUp68ci4M'
bot = Bot(token = API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
 
# Определим группы состояний 
class QuizQuestions(StatesGroup):
    Q1 = State()
    Q2 = State()
    Q3 = State()
    Q4 = State()
    Q5 = State()
    END = State()
 
# Вопросы и ответы
quiz_questions = {
    'What is the capital of France': 'Paris',
    'What is the largest country in the world by land area?': 'Russia',
    'What is the currency of Japan?': 'Yen',
    'What is the capital of Malta':'Valetta',
    'What is the biggest animal in the world':'blue whale'
}
 
@dp.message_handler(commands=['start'])
async def start_message_handler(message: types.Message):
    # Обнулим состояние опросника
    await QuizQuestions.END.set()
 
    # Задаем первый вопрос
    await message.answer('Welcome to Quiz! Lets go. What is the capital of France? ')
    # задать состояние для Q1
    await QuizQuestions.Q1.set()
 
@dp.message_handler(state=QuizQuestions.Q1)
async def handle_q1_answer(message: types.Message, state: FSMContext):
    # ответ юзера
    answer = message.text.lower()
 
    if answer == quiz_questions['What is the capital of France'].lower():
        await message.answer("🎉 Correct! What is the largest country in the world by land area?")
        # установка текущего стейта
        await QuizQuestions.Q2.set()
    else:
        await message.answer("🥲 Sorry, thats incorrect. Try again please, better luck next time")
        # установка текущего стейта
        await QuizQuestions.Q1.set()
 
 
@dp.message_handler(state=QuizQuestions.Q2)
async def handle_q2_answer(message: types.Message, state: FSMContext):
    answer = message.text.lower()
 
    if answer == quiz_questions['What is the largest country in the world by land area?'].lower():
        await message.answer("🎌 Correct! What is the currency of Japan?")
        await QuizQuestions.Q3.set()
    else:
        await message.answer("🥲 Sorry, thats incorrect. Try again please, we believe that you can!")
        # установка текущего стейта
        await QuizQuestions.Q2.set()
    
 
@dp.message_handler(state=QuizQuestions.Q3)
async def handle_q3_answer(message: types.Message, state: FSMContext):
    answer = message.text.lower()
 
    if answer == quiz_questions['What is the currency of Japan?'].lower():
        await message.answer("What is the capital of Malta")
        await QuizQuestions.Q4.set()
    else:
        await message.answer("Sorry, thats incorrect. Try again later 🏞️")

@dp.message_handler(state=QuizQuestions.Q4)
async def handle_q4_answer(message: types.Message, state: FSMContext):
    answer = message.text.lower()
 
    if answer == quiz_questions['What is the capital of Malta'].lower():
        await message.answer("What is the biggest animal in the world")
        await QuizQuestions.Q5.set()
    else:
        await message.answer("Sorry, thats incorrect. Try again later 🏞️")

@dp.message_handler(state=QuizQuestions.Q5)
async def handle_q4_answer(message: types.Message, state: FSMContext):
    answer = message.text.lower()
 
    if answer == quiz_questions['What is the biggest animal in the world'].lower():
        await message.answer("🎊 🎊 🎊 Congratulations, you completed the quiz! 🎊 🎊 🎊")
        await QuizQuestions.END.set()
    else:
        await message.answer("Sorry, thats incorrect. Try again later 🏞️")

 
 
@dp.message_handler(state=QuizQuestions.END)
async def handle_end_state(message: types.Message):
    await message.answer("The quiz has ended. Type /start to take the quiz again.")
 
        
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
    
 

