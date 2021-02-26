from . import views
from django.urls import path
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('show', views.show_user_profile, name='show_user_profile'),
    path('create-profile', views.create_user_profile, name='user-create-profile'),
    path('orders', views.user_orders, name='user-orders'),
    path('saved-items', views.user_saved_items, name='user-saved-items'),
]