from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def print_hello_world(request):
    return HttpResponse(request, "<h2>Hello world<h2/>",)