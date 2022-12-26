from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def first (request):
    return HttpResponse("""<h1><marquee><br>madhura is a good gril</br> <br>shana is a cute gril</br> <br>savitha is a kid</br></marquee></h1> """)
