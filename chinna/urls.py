from django.urls import path
from chinna.views import *
app_name="something"

urlpatterns=[
    path('first/',first,name='first'),
]