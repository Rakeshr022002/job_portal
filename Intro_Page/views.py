from django.shortcuts import render

# Create your views here.

def Intro(request):
    return render(request,"intro.html")