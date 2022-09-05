from http.client import HTTPResponse
from operator import truediv
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hello(request):
    return HTTPResponse("Hello World")



    