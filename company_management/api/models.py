from django.db import models

# Create your models here.

class Departments(models.Model):
    name = models.CharField(max_length=50)
    dept_id = models.CharField(max_length=10)
    description = models.TextField()

    def __str__(self) :
        return self.name + '(' + self.dept_id + ')'

class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    dept_id = models.ForeignKey(Departments,on_delete=models.SET_NULL,null=True)
    position = models.CharField(max_length=50)
    manager_id = models.ForeignKey('self', on_delete = models.SET_NULL,null=True)

    def __str__(self) :
        return self.first_name+' '+self.last_name