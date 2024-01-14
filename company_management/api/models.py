from django.db import models
import uuid
# Create your models here.

class Department(models.Model):
    name=models.CharField(max_length=50, unique=True)
    id=models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)

    description=models.TextField(blank=True)

    def __str__(self):
        return 'Department name: '+self.name + ' ,Department description: '+self.description


class Employee(models.Model):
    firt_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    id=models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    email=models.EmailField()
    role=models.CharField(max_length=20)
    department=models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    manager_id=models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True)


    def __str__(self):
        return self.firt_name + ' ' + self.last_name