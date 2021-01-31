from django.urls import path
from . import views


urlpatterns = [
    path('get_rooms_marks/', views.get_room),
    path('get_rooms_marks/<str:room>', views.get_marks_from_room),
]
