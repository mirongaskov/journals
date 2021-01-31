from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login),
    path('confirm_email/<str:code>', views.confirm_email),
    path('registration/', views.registration),
]
