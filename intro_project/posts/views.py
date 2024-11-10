"""
Views File.
"""
#from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    """
    Handles getting an HHTP request and sends a HTTP response
    """
    return HttpResponse("Hello, world. You're at the posts index.")
