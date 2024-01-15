from django.http import JsonResponse
from .models import Employee
import json


#create a department
def createEmployee(request):
    
    body = json.loads(request.body.decode('utf-8'))
    if 'email' not in body :
        return JsonResponse({'status': 'fail','message': 'email required'},status=400)
    try:
        Employee.objects.create(firt_name=body['firt_name'],
                                last_name=body['last_name'],
                                email=body['email'],
                                role=body['role'],
                                department_id=body['department_id'],
                                manager_id=body['manager_id'])

    except Exception as e:

        data={
            'status': 'fail',
            'message': str(e)
        }
        return JsonResponse(data, status=400)
    
    data={
        'status': 'success',
        'message': 'Employee added!',
    }
    return JsonResponse(data, status=201)
