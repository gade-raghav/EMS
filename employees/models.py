from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.

class Employee(models.Model):
    employee_name = models.CharField(max_length=200)
    unique_id = models.AutoField(primary_key=True)
    employee_id = models.IntegerField(unique=True,validators=[MaxValueValidator(99999999),MinValueValidator(10000000)])
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.employee_id)

