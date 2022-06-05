from django.shortcuts import render
from django.http  import HttpResponse
import datetime as dt
from .models import  Images,Profile, likes

# Create your views here.
def index(request):
    return render(request,'index.html')



def profile_today(request):
    date = dt.date.today()
    profile = Images.todays_profile()
    profile = likes.objects.all()

    return render(request, 'home/profile.html', {"profile":profile,"date": date})





def search_results(request):

    if 'images' in request.GET and request.GET["images"]:
        search_term = request.GET.get("images")
        searched_images = Images.search_by_image_name(search_term)
        message = f"{search_term}"

        return render(request, 'home/search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'home/search.html',{"message":message})