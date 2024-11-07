from django.shortcuts import render

from django.http import HttpResponse

# This is solely to test to see if my (JP's) branches work

def index(request):
    return HttpResponse("Hello, world. You're at the posts index.")
