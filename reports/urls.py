from django.urls import path

from . import views

urlpatterns = [
    path('', views.send_report, name="send_report"),
    path('report/<int:report_id>/', views.report_detail, name='report_detail'),
]