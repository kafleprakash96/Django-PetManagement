from django.http.response import Http404
from django.shortcuts import render

from django.http import Http404

from .models import Pet

def home(request):
    pets = Pet.objects.all()
    return render(request,'home.html' ,{
        'pets' : pets,
    })

def pet_detail(request,pet_id):
    try:
        pet = Pet.objects.get(id=pet_id)
    except:
        raise Http404("Pet Not found")
    return render(request,'pet_detail.html',{
        'pet' : pet,
    })

