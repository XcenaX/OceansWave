# -*- coding: utf-8 -*-
from django.conf import settings
import datetime
from os import name
import telebot
import requests
from threading import Thread
from django.template.loader import render_to_string

class Bot():
    owners_file = "bot_data/owners.txt"
    users_file = "bot_data/users.txt"
    token = ""
    channel_name = ""
    
    def __init__(self, settings):
        self.token = settings["bot_token"]
        self.channel_name = settings["channel_name"]
        self.owners_file = settings["BASE_DIR"]/self.owners_file
        self.users_file = settings["BASE_DIR"]/self.users_file

    def send_msg(self, text):
        url_req = "https://api.telegram.org/bot" + self.token + "/sendMessage" + "?chat_id=@" + self.channel_name + "&text=" + text  + "&parse_mode=html"
        requests.get(url_req)        

    def send_event(self, event):
        message_html = render_to_string('telegram_message.html', {
            'event': event
        })
        self.send_msg(message_html)
        
   

