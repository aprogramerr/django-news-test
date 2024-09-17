from django.shortcuts import render , get_object_or_404
from app_news.models import News
from django.contrib.auth import  get_user_model
from django.core.paginator import Paginator

User = get_user_model()

def index(request):
    all_news = News.objects.filter(status='pb')
    paginator = Paginator(all_news, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'last_news': News.objects.filter(status='pb').order_by('-publish_datetime')
    }
    return render(request, 'index.html', context)

def news(request, id):
    context = {
        'news': News.objects.get(id=id)
    }
    return render(request, 'news.html', context)

def author(request, id):
    context = {
        'author': User.objects.get(id=id)
    }
    return render(request, 'author.html', context)

