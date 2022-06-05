from django.shortcuts import render
from django.http  import HttpResponse
import datetime as dt
# from .models import  Images

# Create your views here.
def index(request):
    return render(request,'index.html')



def profile(request):
    date = dt.date.today()
    # profile = Images.profile()
    return render(request, 'instagram/profile.html', {"date": date,"post":profile})