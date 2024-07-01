import json
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Blog Home</h1>')

def about(request):
    return HttpResponse('<h1>Blog About</h1>')

def messaging(request):
    return HttpResponse(json.dumps({'message': 'Hello, World!'}), content_type='application/json')
