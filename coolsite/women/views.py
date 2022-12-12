from django.http import HttpResponse, HttpResponseNotFound, Http404

from django.shortcuts import render, redirect


def index(request):
    return HttpResponse("Сраница приложения women")


def categories(request, catid):
    if (request.GET):
        print(request.GET)

    return HttpResponse(f"<h1>Статьи по категориям</h1><p>{catid}</p>")


def archive(request, year):
    if int(year) > 2020:
        return redirect('/', permanent=True)

    return HttpResponse(f"<h1>Архив по городам</h1><p>{year}</p>")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
