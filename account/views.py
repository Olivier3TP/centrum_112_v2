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
    reports = Report.objects.filter(assigned_to=request.user)
    return render(request, 'account/medic_dashboard.html', {'reports': reports, 'medic': request.user})
@login_required
def dispatcher_dashboard(request):
    reports = Report.objects.all()
    medics = CustomUser.objects.filter(role='medic')

    if request.method == 'POST':
        report_id = request.POST.get('report_id')
        medic_id = request.POST.get('medic_id')

        try:
            report = Report.objects.get(id=report_id)
            medic = CustomUser.objects.get(id=medic_id, role='medic')
            report.assigned_to = medic
            report.save()
        except (Report.DoesNotExist, CustomUser.DoesNotExist):
            return HttpResponse("Niepoprawne dane.", status=400)

    return render(request, 'account/dispatcher_dashboard.html',{'reports': reports, 'medics': medics, 'dispatchers': request.user})

def home(request):
    return render(request, 'home.html')