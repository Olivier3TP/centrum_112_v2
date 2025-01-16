from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from account.models import CustomUser
from reports.forms import ReportForm
from reports.models import Report


# Create your views here.
def send_report(request):
    if request.method == "POST":
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = ReportForm()
            messages.success(request, 'Twoje zgłoszenie zostało wysłane')
    else:
        form = ReportForm()
    return render(request, 'reports/send_report.html', {'form': form})

# @login_required
def report_detail(request, report_id):
    # report = get_object_or_404(Report, id=report_id)
    # return render(request, 'reports/report_detail.html', {'report': report})
    report = get_object_or_404(Report, id=report_id)
    medics = CustomUser.objects.filter(role='medic')
    user_role = getattr(request.user, 'role', None)

    if user_role == 'dispatcher':
        back_url = 'dispatcher_dashboard'
    elif user_role == 'medic':
        back_url = 'medic_dashboard'

    if request.method == 'POST':
        medic_id = request.POST.get('medic_id')
        try:
            medic = CustomUser.objects.get(id=medic_id, role='medic')
            report.assigned_to = medic
            report.save()
            messages.success(request, f'{medic.username} został przypisany do zgłoszenia.')
        except CustomUser.DoesNotExist:
            return HttpResponse("Niepoprawne dane medyka.", status=400)

    return render(request, 'reports/report_detail.html', {'report': report, 'medics': medics, 'back_url': back_url})