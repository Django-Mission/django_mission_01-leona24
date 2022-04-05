from random import Random, random
from re import template
import re
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
from django.core.handlers.wsgi import WSGIRequest
import requests
import random


# Create your views here.
def lottoresult(request):
    num = int(request.GET.get('count'))
    result = []
    list = []
    for i in range(0, num):
        for i in range(0, 6):
            lottoNum = random.randint(1, 45)
            list.append(lottoNum)
        result.append(random.sample(list, 6))
        list.clear

    # 3. 응답
    return render(request, 'result.html', {"result" : result})
