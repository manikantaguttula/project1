from django.test import TestCase
from .models import items

class Basictests(TestCase):
    def setup(self):
        items.objects.create(name='MRFtyres',
                            descrption='MRF tyres is one of leading product in marrket.',
                            costperitem= 600,
                            stockquantity= 6,
                            volume= 3600.00)
    def test_get_method(self):
        url="http://127.0.0.1:8000/students/"
        response=self.client.get(url)
        self.assertEqual(response.status_code,200)
        qs=items.objects.filter(name='MRFtyres')
        self.assertEqual(qs.count(),1)
# Create your tests here.
