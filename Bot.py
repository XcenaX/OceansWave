# -*- coding: utf-8 -*-
from django.conf import settings
import datetime
from os import name
import telebot
from telebot import TeleBot, types

from threading import Thread
from django.template.loader import render_to_string

class Bot():
    owners_file = "bot_data/owners.txt"
    users_file = "bot_data/users.txt"
    bot = None
    channel_name = ""
    
    def __init__(self, settings):
        self.bot = telebot.TeleBot(settings["bot_token"])
        self.channel_name = settings["channel_name"]
        self.owners_file = settings["BASE_DIR"]/self.owners_file
        self.users_file = settings["BASE_DIR"]/self.users_file
         

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

    def add_user(self, id):
        id = str(id)
        users = self.get_users()
        if id not in users:
            with open(self.users_file, "a") as f:
                f.write("\n"+id)

    def check_owner(self, name):
        name = str(name)
        owners = self.get_owners()
        if name in owners:
            return True
        return False

    def check_date_format(self, date):        
        try:
            datetime.datetime.strptime(date, "%Y.%m.%d %H:%M")
        except:
            return False
        return True


    def get_main_keyboard(self):
        keyboard = types.InlineKeyboardMarkup() 
        add_new = types.InlineKeyboardButton(text="Сделать рассылку", callback_data="add_new")
        keyboard.add(add_new)
        return keyboard

    def make_mailing(self, message):
        self.bot.send_message(chat_id="@%s" % self.channel_name, text=message.text)
        self.bot.send_message(message.from_user.id, "Я закончил рассылку\nЧто дальше?",  reply_markup=self.get_main_keyboard())

    def send_event(self, event):
        users = self.get_users()
        message_html = render_to_string('telegram_message.html', {
            'event': event
        })
        self.bot.send_message(chat_id="@%s" % self.channel_name, text=message_html, parse_mode="html")
        # for user in users:         
        #     bot.send_message(user, text=event_text, parse_mode="html")   
        
    def start_bot(self):
        thread = Thread(target = self.bot.polling, args = (True, 0))
        thread.start()

