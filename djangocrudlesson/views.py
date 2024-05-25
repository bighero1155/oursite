from django.shortcuts import render, redirect
from .models import Gender, User
from django.contrib import messages
from django.contrib.auth.hashers import make_password

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

def show_gender(request, gender_id):
    gender = Gender.objects.get(pk=gender_id)  #select * from genders where gender_id = gender_id

    context = {
        'gender': gender,
    } 
    return render(request, 'gender/show.html', context)

def edit_gender(request, gender_id):
    gender = Gender.objects.get(pk=gender_id)  #select * from genders where gender_id = gender_id

    context = {
        'gender': gender,
    } 
    
    return render(request, 'gender/edit.html', context)

def update_gender(request, gender_id):
    gender = request.POST.get('gender')
    
    Gender.objects.filter(pk=gender_id).update(gender=gender) #update genders set gender = gender where gender_id = gender_id
    messages.success(request, 'Gender successsfully updated.')

    return redirect('/genders')

def delete_gender(request, gender_id):
    gender = Gender.objects.get(pk=gender_id)  #select * from genders where gender_id = gender_id

    context = {
        'gender': gender,
    } 
    
    return render(request, 'gender/delete.html', context)

def destroy_gender(request, gender_id):
    Gender.objects.filter(pk=gender_id).delete() # delete from genders where gender_id = gender_id
    messages.success(request, 'Gender successfully deleted.')

    return redirect('/genders')

def index_user(request):
    users = User.objects.select_related('gender')

    context = {
        'users': users,
    }

    return render(request, 'user/index.html', context)

def create_user(request):
    genders = Gender.objects.all() 

    context = {
        'genders': genders
    }

    return render(request, 'user/create.html', context)

def store_user(request):
    firstName = request.POST.get('first_name')
    middleName = request.POST.get('middle_name')
    lastName = request.POST.get('last_name')
    age = request.POST.get('age')
    birthDate = request.POST.get('birth_date')
    genderId = request.POST.get('gender_id')
    username = request.POST.get('username')
    password = request.POST.get('password')
    confirmPassword = request.POST.get('confirm_password')

    if password == confirmPassword:
        encryptedPassword = make_password(password)

        User.objects.create(first_name=firstName, middle_name=middleName, last_name=lastName, age=age, birth_date=birthDate,
        gender_id=genderId, username=username, password=encryptedPassword)

        messages.success(request, 'User successfully saved.')

        return redirect('/users')
    else:
        messages.error(request, 'Password do not match.')
        return redirect('/users/create')
 
