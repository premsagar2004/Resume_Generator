from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            pass
            if User.objects.filter(username=username).exists():
                messages.error(request, f'Username: {username} already exists! Please try different username!')
                return redirect('userRegister')

            elif User.objects.filter(email=email).exists():
                messages.error(request, f'Email: {email} already exists! Please try different email!')
                return redirect('userRegister')

            else:
                user = User.objects.create_user(username=username, password=password1, email=email,first_name=first_name,last_name=last_name)
                user.save()
                messages.success(request, f'{first_name} your account has been created. You may now Login')
                return redirect('userLogin')
        else:
            messages.error(request, f'Password does not match. Please try again!')
            return redirect('userRegister')

    return render(request, 'registration/registration.html')



def userLogin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')

        else:
            messages.error(request, 'Invalid Credentials!')
            return redirect('userLogin')


    return render(request, 'registration/login.html')
