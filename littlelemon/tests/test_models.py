from django.test import TestCase
from restaurant.models import Booking,Menu

class Test_Menu_Create(TestCase):
    def test_create_item(self):
        item = Menu.objects.create(Title='Pasta',Price=10,Inventory=12)
        self.assertEqual(item.Title,'Pasta')
        self.assertEqual(item.Price, 10)
        self.assertEqual(item.Inventory,12 )
        return item

class Test_Check(TestCase):
    def test_checkSelf(self):
        question = 5 + 1
        self.assertEqual(question,6)