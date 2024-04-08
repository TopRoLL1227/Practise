from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

zodiac_dict = {
    'leo': 'Лев',
    'cancer': 'Рак',

}


# def get_describe_zodiac(request, describes_zodiac):
#     description = zodiac_dict.get(describes_zodiac, None)
#     if description:
#         return HttpResponse(description)
#     else:
#         return HttpResponseNotFound(f"Невідомий - {describes_zodiac}")

def get_describe_zodiac(request, describes_zodiac: str):
    rdy_describe_dict = zodiac_dict.get(describes_zodiac)
    data = {
        'describes': rdy_describe_dict,
        'title': describes_zodiac,
    }
    return render(request, 'app/info.html', context=data)


def get_describe_zodiac_by_number(request, describes_zodiac):
    zodiac_list = list(zodiac_dict)
    if describes_zodiac > len(zodiac_list):
        return HttpResponseNotFound(f'Not Found')
    zodiac = zodiac_list[describes_zodiac - 1]
    redirect_url = reverse('name1', args=[zodiac])
    return HttpResponseRedirect(redirect_url)


# def index(request):
#     description = list(zodiac_dict)
#     res = ''
#     for x in description:
#         redirect_path = reverse('name1', args=[x])
#         res += f"<li><a href={redirect_path}> {x} </a> </li>"
#     result = f"""
#         <ol>
#             {res}
#         </ol>
#     """
#     return HttpResponse(result)


def index(request):
    description = list(zodiac_dict)
    context = {
        'description': description
    }
    return render(request, 'app/index.html', context=context)