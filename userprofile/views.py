import json

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect

from . import models
import datetime
from .forms import UserProfileForm


# Create your views here.
def show_user_profile(request):
    return render(request, 'userprofile/show-profile.html')

#def create_user_profile(request):



def create_user_profile(request):
    user = request.user
    data = {'user': user}
    if request.method == 'GET':
       return render(request, 'userprofile/create-profile.html', data)

    if request.method == 'POST':
        username = request.POST['username']
        email = request.user.email
        phone = request.POST['phone']
        date = request.POST['date']
        profile_image = request.POST['profile_image']
        gender = request.POST['gender']

        if not username:
            messages.error(request, 'Username is required')
        if not phone:
            messages.error(request, 'Phone is required')
        if not date:
            messages.error(request, 'Date is required')
        if not profile_image:
            messages.error(request, 'Profile image is required')
        if not gender:
            messages.error(request, 'Gender is required')
        else:
            if models.UserProfile.objects.filter(owner=user):
                messages.error(request, 'Profile already exist!')
                return redirect('show_user_profile')
            else:
                models.UserProfile.objects.create(owner=request.user, phone=phone,
                                                  gender=gender, birth_date=date)
                messages.success(request, 'Profile created successfuly')
                return render(request, 'userprofile/show-profile.html', data)

        return render(request, 'userprofile/create-profile.html', data)


def edit_user_profile(request):
    pass


def update_user_profile(request):
    pass

def user_orders(request):
    return render(request, 'userprofile/orders.html')

def user_saved_items(request):
    return render(request, 'userprofile/saved-items.html')