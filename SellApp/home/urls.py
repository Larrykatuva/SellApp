from . import views
from django.urls import path
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('', views.index, name='home'),
]