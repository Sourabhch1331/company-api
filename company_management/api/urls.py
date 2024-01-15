from django.urls import path
from . import views


urlpatterns = [
    path('',views.index, name='index'),
    path('department/<str:pk>',views.departmentHandlerUD, name='department'),
    path('department',views.departmentHandlerCR,name='department'),
    path('employee',views.employeeHandlerCR, name='employee')
]