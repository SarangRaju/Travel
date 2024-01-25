from django.http import HttpResponse
from django.shortcuts import render
from . models import place,profile
# Create your views here.
def hello(request):
    obj=place.objects.all()
    obj2=profile.objects.all()
    return render(request,"index.html",{'result':obj,'pro':obj2})
