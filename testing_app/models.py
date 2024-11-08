from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(max_length=100000)


    def __str__(self):
        return self.name
    







class Testing(models.Model):
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=10000)



    def __str__(self):
        return self.name