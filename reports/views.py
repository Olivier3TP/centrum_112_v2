from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from reports.forms import ReportForm
from reports.models import Report


# Create your views here.
def send_report(request):
    if request.method == "POST":
        form = ReportForm(request.POST)
        if form.is_valid():
            form.save()
            form = ReportForm()
    else:
        form = ReportForm()
    return render(request, 'reports/send_report.html', {'form': form})

# @login_required
def report_detail(request, report_id):
    report = get_object_or_404(Report, id=report_id)
    return render(request, 'reports/report_detail.html', {'report': report})