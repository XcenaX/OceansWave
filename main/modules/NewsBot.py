import telebot
from main.models import Event

class Bot():
    owners_file = "owners.txt"
    users_file = "users.txt"
    bot = None

    def __init__(self, token):
        self.bot = telebot.TeleBot(token)

    def get_owners(self):
        with open(self.owners_file) as f:
            content = f.readlines()
        content = [x.strip() for x in content] 
        return content

    def get_users(self):
        with open(self.users_file) as f:
            content = f.readlines()
        content = [x.strip() for x in content] 
        return content

    def check_owner(self, name):
        owners = self.get_owners()
        if name in owners:
            return True
        return False

    def check_date_format(self, date):
        if date == 1:
            print("tetsfgef")

    def add_new(self, data):
        print("add_new")
    
    def message_handler(self, message):
        if self.check_owner(message.from_user.username):
            if message.text == "Добавить новость":
                print("add_new")
        else:
            self.bot.send_message(message.from_user.id, "Я не могу отвечать на сообщения!\nЯ могу только рассылать новости!")

    
