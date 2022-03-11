from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django import template


from .forms import NewsForm

from news_app.models import NewsContent
import math

# Create your views here.

def home(request):
    obj = NewsContent.objects.all()
    n = len(obj)
    n_slides = n//4 + math.ceil((n/4)-(n//4))
    context = {
        'obj': obj,
        'n_slides': n_slides,
        'range': range(1,n_slides),
    }
    return render(request,'index.html',context)


def news(request, pk):
    obj = NewsContent.objects.get(id=pk)
    tags = obj.tags.all()
    # print('obj:', obj)
    context = {
        'obj': obj,
        'tags': tags,
    }
    return render(request, 'single-news.html', context)


def createNews(request):
    form = NewsForm()

    if request.method == 'POST':
        # print(request.POST)
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'form': form
    }
    return render(request,"news_app_form.html", context)


def updateNews(request,pk):
    news = NewsContent.objects.get(id=pk)
    form = NewsForm(instance=news)

    if request.method == 'POST':
        # print(request.POST)
        form = NewsForm(request.POST, instance=news)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'form': form
    }
    return render(request,"news_app_form.html", context)

def deleteNews(request, pk):
    object = NewsContent.objects.get(id=pk)
    if request.method == 'POST':
        object.delete()
        return redirect('home')
    context = {'object': object}
    return render(request, 'delete_template.html', context)


def nation(request):
    return render(request,'nation.html')