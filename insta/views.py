from django.shortcuts import render
from django.http  import HttpResponse
import datetime as dt
from .models import  Images,Profile, likes

# Create your views here.
def index(request):
    return render(request,'index.html')



def profile(request):
    images = Images.objects.all()()
    profile = likes.objects.all()

    return render(request, 'instagram/profile.html', {"images":images,"profile":profile,})


