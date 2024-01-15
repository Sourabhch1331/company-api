from django.http import JsonResponse
from .models import Employee
import json


#create a department
def createEmployee(request):
    
    body = json.loads(request.body.decode('utf-8'))
    if 'email' not in body :
        return JsonResponse({'status': 'fail','message': 'email required'},status=400)
    try:
        Employee.objects.create(
            firt_name=body['firt_name'],
            last_name=body['last_name'],
            email=body['email'],
            role=body['role'],
            department_id=body['department_id'],
            manager_id=body['manager_id']
        )

    except Exception as e:

        data={
            'status': 'fail',
            'message': str(e)
        }
        return JsonResponse(data, status=400)
    
    return JsonResponse({
        'status': 'success',
        'message': 'Employee added!'
        }, status=201)


def getAllEmployees(request):
    try:
        all_emp = Employee.objects.all().values()

        return JsonResponse({
            'status': 'success',
            'message': 'data fetched!',
            'results': len(list(all_emp)),
            'data': list(all_emp)
        },status=200)
    except Exception as e:
        return JsonResponse({
            'status': 'fail',
            'message': str(e)
        },status=400)

#update department with ID=pk
def updateEmployee(request,id):

    try:
        emp = Employee.objects.get(pk=id)
        data=json.loads(request.body)
    except Employee.DoesNotExist:
        return JsonResponse({'status': 'fail', 'message': 'Not Found'}, status=404)
    
    for key,value in data.items():
        print(key)
        setattr(emp,key,value)
    emp.save()
    return JsonResponse({'status': 'success', 'message': 'updated!'},status=204)



