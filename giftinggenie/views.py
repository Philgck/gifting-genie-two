from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required
def home(request):
    user = request.user
    return redirect('myaccount_home', user_id=user.id)