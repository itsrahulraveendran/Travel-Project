from django.http import HttpResponse
from django.shortcuts import render
from . models import places
from . models import team
# Create your views here.
def web(request):
    obj=places.objects.all()
    crew=team.objects.all()
    return render(request,"index.html",{"result":obj,"teammember":crew})

def head(request):
    # return HttpResponse("This is heading")
    return render(request,"index.html")
def website(request):
    return render(request,"website.html")