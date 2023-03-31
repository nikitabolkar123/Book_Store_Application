from django.urls import reverse
from tests.test_setup import TestSetUp


class TestCartItem(TestSetUp):

    def test_create_valid_cart_item_with_jwt_auth(self):
        token = self.get_token()
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        response = self.client.post(self.book_url, self.book_data, format='json')
        book_id = response.data.get('data').get('id')  # dict get id from data
        cart_item = {
            "book": book_id,
            "quantity": 2
        }
        response = self.client.post(self.cart_item_url, cart_item, format="json")
        self.assertEqual(response.status_code, 201)

    def test_create_invalid_cart_item_with_jwt_auth(self):
        token = self.get_token()
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        # book id does not exist
        cart_item = {
            "book": 9999,
            "quantity": 2
        }
        response = self.client.post(self.cart_item_url, cart_item, format="json")
        # we r intentionally making the test fail by asserting a wrong status code
        self.assertEqual(response.status_code, 400)

    def test_create_cart_item_missing_fields(self):
        token = self.get_token()
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        response = self.client.post(self.book_url, self.book_data, format='json')
        book_id = response.data.get('data').get('id')  # dict get id from data
        cart_item = {
            "book": book_id,  # we r missing quantity field
        }
        response = self.client.post(self.cart_item_url, cart_item, format="json")
        self.assertEqual(response.status_code, 400)

    def test_get_items(self):
        token = self.get_token()
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        response = self.client.post(self.book_url, self.book_data, format='json')
        book_id = response.data.get('data').get('id')
        cart_item = {
            "book": book_id,
            "quantity": 2
        }
        res = self.client.post(self.cart_item_url, cart_item, format="json")
        cart_id = res.data.get('data').get('cart')
        cart_url = reverse('cart_item_api', args=[cart_id])
        response = self.client.get(cart_url)
        self.assertEqual(response.data.get("status"), 200)

    def test_cart_item_delete_(self):
        token = self.get_token()
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        response = self.client.post(self.book_url, self.book_data, format='json')
        book_id = response.data.get('data').get('id')
        cart_item = {
            "book": book_id,
            "quantity": 2
        }
        res = self.client.post(self.cart_item_url, cart_item, format="json")
        cart_item_id = res.data.get('data').get('id')
        delete_url = reverse('cart_item_delete_api', args=[cart_item_id])
        response = self.client.delete(delete_url, format='json')
        self.assertEqual(response.data.get('status'), 204)

    def test_cart_item_delete_failure(self):
        token = self.get_token()
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        # create a cart item
        response = self.client.post(self.book_url, self.book_data, format='json')
        book_id = response.data.get('data').get('id')
        cart_item = {
            "book": book_id,
            "quantity": 2
        }
        res = self.client.post(self.cart_item_url, cart_item, format="json")
        cart_item_id = res.data.get('data').get('id')
        # try to delete the cart item with an invalid token
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + 'invalid_token')
        delete_url = reverse('cart_item_delete_api', args=[cart_item_id])
        response = self.client.delete(delete_url, format='json')
        # intentionally  we making the test fail by asserting a wrong status code
        self.assertEqual(response.status_code, 401)

    def test_cart_item_checkout_(self):
        token = self.get_token()
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        response = self.client.post(self.book_url, self.book_data, format='json')
        book_id = response.data.get('data').get('id')
        cart_item = {
            "book": book_id,
            "quantity": 2
        }
        res = self.client.post(self.cart_item_url, cart_item, format="json")
        checkout_url = reverse('checkout_api')
        response = self.client.put(checkout_url, format='json')
        self.assertEqual(response.data.get('status'), 200)
