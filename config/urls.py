from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.paciente, name='paciente'),
    path('paciente/create/', views.create_pac, name='create_pac'),
]