import random
import string
import datetime
from main.models import *
from django.urls import reverse

def check_image_type(image):
    try:
        if not image.name.endswith(".png") and not image.name.endswith(".jpg"):
            return False
    except:
        return False
    return True

def get_current_user(request):
    try:
        user_id = int(request.session["user"])
        current_user = User.objects.filter(id=user_id).first()
        return current_user
    except:
        return None 

def has_access(request): # Возвращает две переменные: Первая - есть ли доступ, вторая - урл для редиректа если нет доступа
    view_name = request.path.split("/")[1]
    current_user = get_current_user(request)
    if not current_user:
        return False, reverse("main:login")
    role = current_user.role.name
    
    if not role:
        return False, reverse("main:login")
    if role == "worker":
        if view_name in ["profile", "", "quests"]:
            return True, None
        return False, reverse("main:index")
    elif role == "main_worker":
        if view_name in ["main_worker_quests", "main_worker_my_quests", "need_to_check", "create_quest"]:
            return True, None
        return False, reverse("main:main_worker_quests")
    elif role == "accountant":
        if view_name in ["profile", "", "quests"]:
            return True, None
    elif role == "director":
        return True, None
    return False, reverse("main:login")

def is_number(string):
    try:
        string = int(string)
    except:
        return False
    return True

class make_incrementor(object):
    count = 0

    def __init__(self, start):
        self.count = start

    def inc(self, jump=1):
        self.count += jump
        return self.count

    def res(self):
        self.count = 0
        return self.count

class margin_counter(object):
    count = 0
    jump = 0

    def __init__(self, start=0, jump=0):
        self.count = start
        self.jump = jump

    def inc(self):
        self.count += self.jump
        return self.count

    def reset(self):
        self.count = 0
        return self.count

def get_types():
    quests = []
    types = QuestType.objects.all()
    for qtype in types:
        current_quest = {"type": qtype, "categories":[]}
        for category in QuestCategory.objects.filter(quest_type=qtype):
            current_quest["categories"].append(category)
        quests.append(current_quest)
    return quests


def get_paginated_blogs(request, paginator):
    page = request.GET.get('page')
    try:
        page = int(page)
    except:
        page = 1
    a = ""
    block = ""
    pages=[]
    if page:
        try:
            block = paginator.page(page)
        except EmptyPage:
            block = paginator.page(paginator.num_pages)
            page = paginator.num_pages

        for i in range(page-2, page+3):
            try:
                a = paginator.page(i)
                pages.append(i)
            except:
                continue
        print(pages)
        if pages[-1] != paginator.num_pages:
            pages.append(paginator.num_pages)

        if pages[0] != 1:
            pages.insert(0, 1)
    else:
        pages = [1,2,3,4,5,paginator.num_pages]
        block = paginator.page(1)
    return block, pages