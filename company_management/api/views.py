from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from .models import Department, Employee


# Create your views here.
def index(request):
    return HttpResponse('<h2>Hello!</h2>')


#HANDLE CREATE AND READ OPERATIONS
@csrf_exempt
def departmentHandlerCR(request):
    if request.method == 'POST':
        return createDepartment(request)
    elif request.method == 'GET':
        return getAllDepartments(request)
    
    return JsonResponse({'status': 'fail', 'message': 'Route Not Found'}, status=404)

#HANDLE UPDATE AND DELETE OPERATIONS
@csrf_exempt
def departmentHandlerUD(request,pk):
    
    if request.method in ['PATCH','PUT']:
        return updateDepartment(request,pk)
    elif request.method == 'DELETE':
        return deleteDepartment(request,pk)

    return JsonResponse({'status': 'fail', 'message': 'Route Not Found'}, status=404)




#create a department
def createDepartment(request):
    
    body = json.loads(request.body.decode('utf-8'))

    try:
        Department.objects.create(name=body['name'], description=body['description'])

    except Exception as e:

        data={
            'status': 'fail',
            'message': 'field is wrong '+str(e),
        }
        return JsonResponse(data, status=400)
    
    data={
        'status': 'success',
        'message': 'Department created!',
    }
    return JsonResponse(data, status=201)


#Get all Departments
def getAllDepartments(request):
    data={
        'status': 'success',
        'message': 'Data Retrived!'
    }

    allDep=Department.objects.all().values()
    data['results']=len(list(allDep))
    data['data']=list(allDep)    
    
    return JsonResponse(data,status=200)


#update department with ID=pk
def updateDepartment(request,pk):

    try:
        dept = Department.objects.get(pk=pk)
        data=json.loads(request.body)
    except Department.DoesNotExist:
        return JsonResponse({'status': 'fail', 'message': 'Not Found'}, status=404)
    
    for key,value in data.items():
        setattr(dept,key,value)
    dept.save()
    return JsonResponse({'status': 'success', 'message': 'updated!'},status=204)


def deleteDepartment(request,pk):
    try:
        dept = Department.objects.get(pk=pk)
        dept.delete()
    except Department.DoesNotExist:
        return JsonResponse({'status': 'fail', 'message': 'Not Found'}, status=404)
    
    return JsonResponse({'status': 'success', 'message': 'Deleted!'}, status=204)