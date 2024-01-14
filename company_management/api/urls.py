from django.urls import path
from . import views


urlpatterns = [
    path('',views.index, name='index'),
    path('department/<str:pk>',views.departmentHandlerUD),
    path('department',views.departmentHandlerCR),
    
]