from django.shortcuts import render, redirect
from .models import Gender
from django.contrib import messages

# Create your views here.
def index_gender(request):
    genders = Gender.objects.all() #select * from genders

    context = {
        'genders': genders
    }

    return render(request, 'gender/index.html', context)


def create_gender(request):
    return render(request, 'gender/create.html')

def store_gender(request):
    gender = request.POST.get('gender')
    Gender.objects.create(gender=gender) #insert into genders(gender) values(gender)
    messages.success(request, 'Gender successfully saved!')
    return redirect('/genders')