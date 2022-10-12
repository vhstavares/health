from email.policy import default
from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    birth = models.DateField(blank=True, null=True)
    document = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    sale_opportunity = models.BooleanField(default = True)
    
    def __str__(self):
        return self.name

class Vehicle(models.Model):
    
    class ModelsVehicle(models.TextChoices):
        hatch = 'hatch', 'Hatch'
        sedan = 'sedan', 'Sedan'
        convertible = 'convertible', 'Convertible'
    
    class Color(models.TextChoices):
        yellow = 'yellow', 'Yellow'
        blue = 'blue', 'Blue'
        gray = 'gray', 'Gray'
        
    model_vehicle = models.CharField(
        max_length=20, 
        choices=ModelsVehicle.choices, 
        default=ModelsVehicle.hatch
    )
    
    color = models.CharField(
        max_length=20, 
        choices=Color.choices, 
        default=Color.gray
    )
    
    plate = models.CharField(max_length=6, blank=True, null=True)
    year = models.CharField(max_length=4, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)   
    owner = models.ForeignKey(Person, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.plate