from django.test import TestCase
import unittest
from .models import Person, Vehicle

# Create your tests here.
class PersonTestCase(unittest.TestCase):
    def setUp(self):
        self.person = Person.objects.create(
            name = "Maria",
            birth = "1987-01-02",
            document = "325.325.452-52",
            email = "teste@teste.com",
            phone = "(15) 8943-2213",
            sale_opportunity = True
        )
        self.vehicle = Vehicle.objects.create(
            color = 'gray',
            model_vehicle = 'sedan',
            name = 'Corrola',
            plate = 'MKL326',
            year = '2016',
            owner = self.person
        )
    
    def testPerson(self):
        self.assertEquals(self.person.sale_opportunity, True)
    
    def testVehicle(self):
        self.assertEquals(self.vehicle.model_vehicle, 'sedan')