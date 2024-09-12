from django.contrib import admin
from django.urls import path, include
from core.views import calculate_activity, get_materials, create_material, create_result, get_results, delete_results

urlpatterns = [
    path('admin/', admin.site.urls),
    path('calculate_activity/', calculate_activity, name='calculate_activity'),
    path('get_materials/', get_materials, name='get_materials'),
    path('create_material/', create_material, name='create_material'),
    path('create_result/', create_result, name='create_result'),
    path('get_results/', get_results, name='get_results'),
    path('delete_results/', delete_results, name='delete_results'),

]
