from django.shortcuts import render , get_object_or_404
from app_news.models import News

def index(request):
    context = {
        'news_list': News.objects.filter(status='pb'),
        'last_news': News.objects.filter(status='pb').order_by('-publish_datetime')
    }
    return render(request, 'index.html', context)

def news(request, id):
    context = {
        'news': News.objects.get(id=id)
    }
    return render(request, 'news.html', context)

