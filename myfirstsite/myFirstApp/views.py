from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.


def main(request):
    my_str = "Сайт новостей"
    return render(request, 'index.html', {
        'now': datetime.datetime.now(),
        'my_str': my_str
    })


def news(request):
    my_str = "Свежие новости"
    return render(request, 'news.html', {
        'now': datetime.datetime.now(),
        'my_str': my_str
    })
