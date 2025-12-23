from django.db import models

# Create your models here.

class EmployeeModel(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    salary = models.FloatField()
    dept = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"