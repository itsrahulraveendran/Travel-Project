from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect



# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/web')
        else:
            messages.info(request,"invalid user name or password")
            return redirect('login')

    return render(request,'login.html')
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        first_name=request.POST['firstname']
        last_name=request.POST['lastname']
        emailaddress=request.POST['email']
        password=request.POST['password']
        passconfirm=request.POST['passwordconfirm']
        if password==passconfirm:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username Taken")
                return redirect('register')
            elif User.objects.filter(email=emailaddress).exists():
                messages.info(request,"This email already taken")
                return redirect('register')
            else:
                userany=User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name,email=emailaddress)

                userany.save();
                print("user created")
                return redirect('login')


        else:
            # print("Password not matching")
            messages.info(request,"password is not matching")
            return redirect('register')
        return redirect('/web')
    return render(request,"register.html")
def logout(request):
    auth.logout(request)
    return redirect('/web')