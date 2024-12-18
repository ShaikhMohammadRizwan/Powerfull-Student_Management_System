from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('students.urls')),
    path('', include('student.urls')),
    path('', include('home_auth.urls')),
]
