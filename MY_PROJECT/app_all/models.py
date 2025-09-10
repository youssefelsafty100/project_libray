from django.db import models

class Department(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    height = models.IntegerField()
    weight = models.IntegerField()
    salary = models.DecimalField(max_digits=6, decimal_places=2)
    address = models.CharField(max_length=300)
    departments = models.ManyToManyField(Department)

    def __str__(self):
        return self.first_name
 


