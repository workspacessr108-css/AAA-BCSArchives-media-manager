from django.shortcuts import render, HttpResponse 
from django.conf import settings

# Create your views here.
def home_view(request):
    return render (request, "media_manager/index.html", {})