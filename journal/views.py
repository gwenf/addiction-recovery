from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'journal/journal.html')


def entry(request):
    return render(request, 'journal/view.html')


def create(request):
    return render(request, 'journal/create.html')
