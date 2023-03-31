from django.urls import reverse

from book.models import Book
from tests.test_setup import TestSetUp


class TestBook(TestSetUp):
    def test_book_with_blank_list(self):
        token = self.get_token()
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)  # generate bearer token
        # Test retrieving a list of books
        response = self.client.get(self.book_url)  # WE get here list of books
        self.assertEqual(response.status_code, 200)  # Expect a successful response

    def test_create_valid_book_with_jwt_auth(self):
        token = self.get_token()
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        response = self.client.post(self.book_url, self.book_data, format='json')
        self.assertEqual(response.status_code, 201)

    def test_books_list(self):
        token = self.get_token()
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        # create book
        response = self.client.post(self.book_url, self.book_data, format='json')
        # Test retrieving a list of book
        response = self.client.get(self.book_url)
        self.assertEqual(response.status_code, 200)  # Expect a successful response

    def test_create_book_missing_fields(self):
        token = self.get_token()
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        # To Test creating a new book with missing fields
        book_data = {

            "author": "vinay",
        }
        response = self.client.post(self.book_url, book_data, format='json')
        self.assertEqual(response.status_code, 400)

    def test_update_book_success(self):
        token = self.get_token()
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        # Create a book
        response = self.client.post(self.book_url, data=self.book_data, format='json')
        book_id = response.data['data']['id']
        # To Update the book
        updated_book_data = {
            "author": "robin sharma",
            "title": "The Monk Who Sold His Ferrari",
            "price": 200,
            "quantity": 5
        }
        self.update_url = reverse('books', args=[book_id])
        response = self.client.put(self.update_url, data=updated_book_data, format='json')
        self.assertEqual(response.status_code, 200)

    def test_update_book_failure(self):
        token = self.get_token()
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        # Create a book
        response = self.client.post(self.book_url, data=self.book_data, format='json')
        book_id = response.data['data']['id']
        # To Update the note with invalid data
        updated_book_data = {
            "author": "robin sharma",
            "title": "The Monk Who Sold His Ferrari",
            "price": "invalid_price",
            "quantity": -1
        }
        self.update_url = reverse('books', args=[book_id])
        response = self.client.put(self.update_url, data=updated_book_data, format='json')
        self.assertEqual(response.status_code, 400)

    def test_delete_book_success(self):
        token = self.get_token()
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        # To Create a book
        response = self.client.post(self.book_url, data=self.book_data, format='json')
        book_id = response.data['data']['id']
        # Test deleting an existing book
        self.delete_url = reverse('books', args=[book_id])
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, 200)  # Expect a successful delete response
        self.assertEqual(Book.objects.count(), 0)  # tests whether the number of records in the Book table is equal to 0

    def test_delete_book_failure(self):
        token = self.get_token()
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        # Test deleting a non-existent book
        self.delete_url = reverse('books', args=[1000])  # Using an ID that does not exist in the database
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, 400)  # Expect a not found response
