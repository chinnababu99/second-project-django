from django.urls import path
from chinna1.views import *
app_name="something"

urlpatterns=[
    path('second/',second,name='sceond'),
]