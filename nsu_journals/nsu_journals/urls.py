from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cleaning_journal/', include('cleaning_journal.urls')),
    path('authorization/', include('authorization.urls')),
    path('profile/', include('user_profile.urls')),
    path('', include('homepage.urls')),
]
