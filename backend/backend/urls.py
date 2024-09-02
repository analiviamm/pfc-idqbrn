from django.contrib import admin
from django.urls import path, include
from core.views import calculate_activity

urlpatterns = [
    path('admin/', admin.site.urls),
    path('calculate_activity/', calculate_activity, name='calculate_activity'),
]
