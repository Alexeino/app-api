from django.test import TestCase

# Create your tests here.
class MyTest(TestCase):
    
    def test_api_response(self):
        response = self.client.get('/api/home/')
        self.assertEqual(response.status_code,200)