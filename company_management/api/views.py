from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
#models
from .models import Department, Employee


# Create your views here.


def index(request):
    return HttpResponse('<h2>Hello!</h2>')

@csrf_exempt
def departmentHandler(request):
    if request.method == 'POST':
        return createDepartment(request)
    elif request.method == 'GET':
        return getAllDepartments(request)
    
    return JsonResponse(data={'status': 'fail', 'message': 'Not Found'}, status=404)


def createDepartment(request):
    
    body = json.loads(request.body.decode('utf-8'))

    try:
        Department.objects.create(name=body['name'], description=body['description'])

    except Exception as e:

        print(e)
        data={
            'status': 'fail',
            'message': 'something went wrong',
        }
        return JsonResponse(data, status=400)
    
    data={
        'status': 'success',
        'message': 'Department created!',
    }
    return JsonResponse(data, status=201)


def getAllDepartments(request):
    data={
        'status': 'success',
        'message': 'Data Retrived!'
    }
    try:
        allDep=Department.objects.all().values()
        
        data['data']=list(allDep)
    except Exception as e:
        print(e)
        data['status']='fail'
        data['message']='something went wrong'

        return JsonResponse(data,status=400)

    return JsonResponse(data,status=200)