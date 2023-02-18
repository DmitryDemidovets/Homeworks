import requests

class Bot():

    def __init__(self,token):
        self.token = token
        self.bot_url = 'https://api.telegram.org/bot{}/'.format(self.token)
        self.bank)url = BANK_API
    
# get_updates

    def get_updates(self):
        method = 'getupdates'
        responce = requsts.get(self.bot_url + method)
        return response.json()

# get_messages

    def get_messages(self):
        data = self.get_updates()
        
