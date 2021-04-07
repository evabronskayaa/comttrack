from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("<h1>Страница регистрации</h1>")


def pageNotFound(request, exception):
    return HttpResponse("<h1>404</h1> <h2>NotFound</h2>")
