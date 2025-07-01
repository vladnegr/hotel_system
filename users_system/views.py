from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

def register_page(request):
    form = UserCreationForm()
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            #return redirect('main')
    return render(request, 'users_system/register.html', context={"form": form})



def login_page(request):
    form = AuthenticationForm()
    if request.method=='POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user is not None:
                login(request, user)
                #return redirect('main')

    return render(request, 'users_system/login.html', context={"form": form})

def logout_page(request):
    if request.user.is_authenticated:
        logout(request)

    return redirect('login')