from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path('', views.send_report, name="send_report"),
    path('report/<int:report_id>/', views.report_detail, name='report_detail'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)