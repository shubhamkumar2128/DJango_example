from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('student/', include('student.urls')),
    path('travel/', include('travel.urls')),
    path('admin/', admin.site.urls),

]
