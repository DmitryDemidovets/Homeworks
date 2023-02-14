import requests
 
TOKEN = '###########'
 
BASE_URL = 'https://api.telegram.org/bot' + TOKEN + '/'
 
# все обновления
def updates():
    current_updates_link = BASE_URL + 'getupdates'
    request = requests.get(current_updates_link)
    return request.json()
 
# из обновлений берем сообщение и айди чата
def message():
    data = updates()
    chat_id = data['result'][-1]['message']['chat']['id']
    last_message = data['result'][-1]['message']['text']
    message_list = {'chat_id': chat_id, 'text': last_message}
    return message_list
 
# отправляем сообщения
def send_message(chat_id, text='...'):
    url =  BASE_URL + 'sendmessage?chat_id={}&text={}'.format(chat_id, text)
    requests.get(url)
 
# обработка команд
def bot_answer():
    answer = message()
    text = answer['text']
    id = answer['chat_id']
 
    if text == '/hi':
        send_message(id, text)
    
    if text == '/joke':
        send_message(id, 'hi there, nice too meet you!')
 
bot_answer()

