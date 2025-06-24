from django.shortcuts import redirect, render
from .forms import SignupForm
from django.contrib.auth import authenticate ,login
from .models import Profile
# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect('accounts/profile')

    else:
        form = SignupForm()
    context = {
        'form':form

    }
    return render(request,'registration/signup.html',context)

def profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request,'accounts/profile.html',{'profile':profile})


def profile_edit(request):
    return render(request,'accounts/profile_edit.html',{})