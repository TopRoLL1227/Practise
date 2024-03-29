from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

zodiac_list = {
    'leo': 'Лев',
    'cancer': 'Рак'

}


def get_describe_zodiac(request, describes_zodiac):
    description = zodiac_list.get(describes_zodiac, None)
    if description:
        return HttpResponse(description)
    else:
        return HttpResponseNotFound(f"Невідомий - {describes_zodiac}")


def get_describe_zodiac_by_number(request, describes_zodiac):
    return HttpResponse(f"Номер - {describes_zodiac}")
