from django.shortcuts import render
from django.shortcuts import HttpResponse

from .models import User

def user_info(request):
    user = User.objects.first()
    return HttpResponse(f"{user.first_name} {user.last_name}, Age: {user.age()}")

