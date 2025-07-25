from django.shortcuts import render
from django.http import HttpResponse



def principal(request):
    return render(request,'principal.html')


# pip3 install Django
# django-admin startproject PROJECT_NAME
# python manage.py runserver