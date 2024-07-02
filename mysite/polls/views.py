from django.shortcuts import render
from django.http import HttpResponse,Http404
# Create your views here.
def index(request):
    return HttpResponse("HI this is your first page")

def second(request):
    return HttpResponse("HI this is your second page")