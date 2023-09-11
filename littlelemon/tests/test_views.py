from django.test import TestCase
from restaurant.models import Booking,Menu
from rest_framework import serializers

class MenuViewTest(TestCase):
        
    def test_generate_items(self):
        item = Menu.objects.create(Title='Pasta',Price=10,Inventory=12)
        item2 = Menu.objects.create(Title='FishLice',Price=19,Inventory=9)
        item3 = Menu.objects.create(Title='ChickenBanaza',Price=22,Inventory=15)
    
    def test_getAll(self):
        items = Menu.objects.all()
        for item in items:
           self.assertEqual(item,serializers.ModelSerializer)
