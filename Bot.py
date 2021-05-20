# -*- coding: utf-8 -*-
from django.conf import settings
import datetime
from os import name
import telebot
from telebot import TeleBot, types

from threading import Thread
from django.template.loader import render_to_string

class Bot():
    bot = None
    channel_name = ""
    
    def __init__(self, settings):
        self.bot = telebot.TeleBot(settings["bot_token"])
        self.channel_name = settings["channel_name"]
        #self.owners_file = settings["BASE_DIR"]/self.owners_file
        #self.users_file = settings["BASE_DIR"]/self.users_file

    def send_event(self, event):
        message_html = render_to_string('telegram_message.html', {
            'event': event
        })
        self.bot.send_message(chat_id="@%s" % self.channel_name, text=message_html, parse_mode="html")
        
   

