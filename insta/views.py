from django.shortcuts import render
from django.http  import HttpResponse
from .models import  Images,Profile, comments, likes
from .forms import InstaLetterForm
from .models import Images, InstaLetterRecipients
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist



# Create your views here.
def index(request):
    
    return render(request,'index.html')



@login_required(login_url='/accounts/login/')
def profile_today(request):
    profile = Images.objects.all()
    if request.method == 'POST':
        form = InstaLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            recipient = InstaLetterRecipients(name = name,email =email)
            recipient.save()
            send_welcome_email(name,email)
            HttpResponseRedirect('profile_today')
            
    else:
        form = InstaLetterForm()
    return render(request, 'home/profile.html', {"profile":profile,"letterForm":form })


@login_required(login_url='/accounts/login/')
def bio_profile(request):
    bio = Profile.objects.all()
    HttpResponseRedirect('bio_today')

    return render(request, 'home/bio.html', {bio:'bio'})


def comment(request):
      comm = comments.objects.all()
      return render  (request,'home/comments.html',{comm:'comm'})







def search_results(request):

    if 'images' in request.GET and request.GET["images"]:
        search_term = request.GET.get("images")
        searched_images = Images.search_by_image_name(search_term)
        message = f"{search_term}"

        return render(request, 'home/search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'home/search.html',{"message":message})



@login_required(login_url='/accounts/login/')
def images(request,images_id):
    try:
        images = Images.objects.get(id = images_id)
    except ObjectDoesNotExist:
        raise Http404()
    return render(request,"home/index.html", {"images":images})

