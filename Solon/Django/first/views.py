from django.http import HttpResponse
from django.shortcuts import render





def index(request):
    msg= "this is the index page"
    return HttpResponse(msg)

def objectives(request):
    return render(request,'objectives.html')

def mission(request):
    return render(request,'mission.html')
def vision(request):
    return render(request,'vision.html')