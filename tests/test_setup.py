from django.urls import reverse
from rest_framework.test import APITestCase, APIClient


class TestSetUp(APITestCase):
    def setUp(self):
        self.book_url = reverse('books')
        self.register_url = reverse('user_registration')
        self.login_url = reverse('login')
        self.token_url = reverse('token_obtain_pair')
        self.cart_item_url = reverse('cart_item_api')

        self.client = APIClient()
        data = {
            "first_name": "abc",
            "last_name": "xyz",
            "email": "abc@gamil.com",
            "location": "sambhajinagar",
            "phone_no": "5667767",
            "username": "sakshi",
            "password": "sakshi",
            "is_superuser": True
        }
        response = self.client.post(self.register_url, data=data)

        self.book_data = {
            "author": "abc",
            "title": "mnop",
            "quantity": 12,
            "price": 120
        }

        self.cart_item_data = {
            "book": 55,
            "quantity": 2
        }

    def tearDown(self):
        return super().tearDown()

    def get_token(self):
        login_data = {'username': 'sakshi', 'password': 'sakshi'}
        response = self.client.post(self.token_url, login_data, format='json')
        self.assertEqual(response.status_code, 200)
        return response.data['access']
