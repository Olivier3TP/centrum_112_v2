from django.urls import path
from account import views

urlpatterns = [
    path('login/', views.user_login, name='user_login'),
    path('medic/', views.medic_dashboard, name='medic_dashboard'),
    path('dispatcher/', views.dispatcher_dashboard, name='dispatcher_dashboard'),
]