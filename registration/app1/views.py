from django.shortcuts import render,HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='login')

# Create your views here.
def HomePage(req):
    return render(req,'home.html')

def SingupPage(req):
    if req.method =='POST':
        uname=req.POST.get('username')
        email=req.POST.get('email')
        pass1= req.POST.get('password1')
        pass2 = req.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect('login')


    return render(req,'signup.html')

def LoginPage(req):
    if req.method == 'POST':
        username = req.POST.get('username')
        pass1 = req.POST.get('pass')
        user = authenticate(req, username=username, password=pass1)
        if user is not None:
            login(req, user)
            return redirect('home')
        else:
            return HttpResponse("Username or Password is incorrect!!!")


    return render(req, 'login.html')


def LogoutPage(request):
    logout(request)
    return redirect('login')

