from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def second(request):
    return HttpResponse("""<h1><marquee><br>mounika is a cute and sweet gril</br></marquee></h1>""")
