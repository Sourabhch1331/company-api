from django.http import JsonResponse
from .models import Department
import json

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


#Delete department with id=pk
def deleteDepartment(request,pk):
    try:
        dept = Department.objects.get(pk=pk)
        dept.delete()
    except Department.DoesNotExist:
        return JsonResponse({'status': 'fail', 'message': 'Not Found'}, status=404)
    
    return JsonResponse({'status': 'success', 'message': 'Deleted!'}, status=204)
