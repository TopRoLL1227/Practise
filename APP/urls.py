from django.urls import path
from . import views

urlpatterns = [
    path('<int:describes_zodiac>/', views.get_describe_zodiac_by_number),
    path('<str:describes_zodiac>/', views.get_describe_zodiac, name='name1'),
]
