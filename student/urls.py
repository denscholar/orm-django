from django.urls import path
from .views import Student_list


urlpatterns = [
    path("", Student_list, name='students'),
]
