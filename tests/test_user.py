from tests.test_setup import TestSetUp


# Create your tests here.
class UserRegistrationTestCase(TestSetUp):

    def test_user_cannot_register_with_no_data(self):
        response = self.client.post(self.register_url)
        self.assertEqual(response.status_code, 400)

    def test_user_registration_with_data(self):
        user_data = {
            "first_name": "Nikita",
            "last_name": "Bolkar",
            "email": "nikita@gmail.com",
            "location": "Aurangabad",
            "phone": "1234567895",
            "username": "nikita",
            "password": "nikita"
        }
        response = self.client.post(self.register_url, data=user_data)
        self.assertEqual(response.status_code, 201)

    def test_user_registration_empty_username_password(self):
        data = {
            "first_name": "Nikita",
            "last_name": "Bolkar",
            "email": "nikita@gmail.com",
            "location": "Aurangabad",
            "phone_no": "1234567895",
            "username": "",
            "password": ""
        }
        response = self.client.post(self.register_url, data=data)
        self.assertEqual(response.status_code, 400)


class LoginTestCase(TestSetUp):

    def test_user_login_success(self):
        user_data = {
            "first_name": "Nikita",
            "last_name": "Bolkar",
            "email": "nikita@gmail.com",
            "location": "Aurangabad",
            "phone": "1234567895",
            "username": "nikita",
            "password": "nikita",
        }

        response = self.client.post(self.register_url, data=user_data)
        login_data = {
            'username': "nikita",
            'password': "nikita"
        }
        response = self.client.post(self.login_url, login_data)
        self.assertEqual(response.status_code, 201)

    def test_user_login_invalid_credentials(self):
        login_data = {
            'username': 'nikita',
            'password': 'sakshi'
        }
        response = self.client.post(self.login_url, login_data)
        self.assertEqual(response.status_code, 400)  # we will Expect an unauthorized response

    def test_user_login_missing_fields(self):
        # to test a login with missing fields
        login_data = {
            'username': 'priyanka'
        }
        response = self.client.post(self.login_url, login_data)
        self.assertEqual(response.status_code, 400)  # Expect a bad request response
