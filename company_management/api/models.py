from django.db import models
import uuid
# Create your models here.

class Department(models.Model):
    name=models.CharField(max_length=50, unique=True)
    id=models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)

    description=models.TextField(blank=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    firt_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    id=models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    email=models.EmailField(unique=True)
    role=models.CharField(max_length=20)
    department_id=models.UUIDField(blank=True,null=True)
    manager_id=models.UUIDField(blank=True,null=True)


    def __str__(self):
        return self.firt_name + ' ' + self.last_name