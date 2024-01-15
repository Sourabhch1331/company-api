from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from .models import Department, Employee
from . import departmentViews
from . import employeeViews

# Create your views here.
def index(request):
    return HttpResponse('<h2>Hello!</h2>')


#HANDLE CREATE AND READ OPERATIONS FOR DEPARTMENT
@csrf_exempt
def departmentHandlerCR(request):
    if request.method == 'POST':
        return departmentViews.createDepartment(request)
    elif request.method == 'GET':
        return departmentViews.getAllDepartments(request)
    
    return JsonResponse({'status': 'fail', 'message': 'Route Not Found'}, status=404)

#HANDLE UPDATE AND DELETE OPERATIONS FOR DEPARTMENT
@csrf_exempt
def departmentHandlerUD(request,pk):
    
    if request.method in ['PATCH','PUT']:
        return departmentViews.updateDepartment(request,pk)
    elif request.method == 'DELETE':
        return departmentViews.deleteDepartment(request,pk)

    return JsonResponse({'status': 'fail', 'message': 'Route Not Found'}, status=404)

#HANDLE CREATE AND READ OPERATIONS FOR EMPLOYEE
@csrf_exempt
def employeeHandlerCR(request):

    if request.method == 'POST':
        return employeeViews.createEmployee(request)

    return JsonResponse({'status': 'fail', 'message': 'Route Not Found'}, status=404)