from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from account import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', views.user_login, name='user_login'),
    path('logout/', auth_views.LogoutView.as_view(), name='user_logout'),
    path('medic/', views.medic_dashboard, name='medic_dashboard'),
    path('dispatcher/', views.dispatcher_dashboard, name='dispatcher_dashboard'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)