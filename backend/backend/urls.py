from django.contrib import admin
from django.urls import path, include
from core.views import calculate_activity, get_materials, create_material

urlpatterns = [
    path('admin/', admin.site.urls),
    path('calculate_activity/', calculate_activity, name='calculate_activity'),
    path('get_materials/', get_materials, name='get_materials'),
    path('create_material/', create_material, name='create_material'),

]
