from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from account.forms import LoginForm
from account.models import CustomUser
from reports.models import Report



# Create your views here.
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            user = authenticate(username=cleaned_data['username'], password=cleaned_data['password'])
            if user is not None:
                login(request, user)
                if user.role == 'medic':
                    return redirect('medic_dashboard')
                elif user.role == 'dispatcher':
                    return redirect('dispatcher_dashboard')
                else:
                    return HttpResponse("Niepoprawna rola użytkownika.", status=400)
            else:
                return HttpResponse("Nieprawidłowe dane logowania", status=401)
    else:
        form = LoginForm()

    return render(request, 'account/login.html', {'form': form})
@login_required
def medic_dashboard(request):
    # if request.method == 'POST' and 'logout' in request.POST:
    #     logout(request)
    #     return render(request, 'home.html')
    pass
@login_required
def dispatcher_dashboard(request):
    reports = Report.objects.all()
    medics = CustomUser.objects.filter(role='medic')
    if request.method == 'POST' and 'logout' in request.POST:
        logout(request)
        return render(request, 'home.html')
    return render(request, 'account/dispatcher_dashboard.html', {'reports': reports, 'medics': medics, 'dispatchers': request.user})

def home(request):
    return render(request, 'home.html')