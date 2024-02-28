# user_profile/tests.py

from django.test import TestCase
from django.urls import reverse
from .models import UserProfile

class UserProfileModelTest(TestCase):

    def setUp(self):
        UserProfile.objects.create(
            first_name='John',
            surname='Doe',
            email='john.doe@example.com',
            phone_number='1234567890'
        )

    def test_user_profile_str(self):
        user_profile = UserProfile.objects.get(email='john.doe@example.com')
        self.assertEqual(str(user_profile), 'John Doe')

class UserProfileViewTest(TestCase):

    def test_create_profile_view(self):
        url = reverse('create_profile')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_profile_form_submission(self):
        url = reverse('create_profile')
        data = {
            'first_name': 'Jane',
            'surname': 'Smith',
            'email': 'jane.smith@example.com',
            'phone_number': '9876543210',
        }
        response = self.client.post(url, data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Profile Created Successfully')

    def test_create_profile_form_validation_email_format(self):
        url = reverse('create_profile')
        invalid_data = {
            'first_name': 'Invalid',
            'surname': 'User',
            'email': 'invalid-email',
            'phone_number': '1234567890',
        }
        response = self.client.post(url, invalid_data)
        self.assertContains(response, 'Enter a valid email address.')
        self.assertContains(response, 'Profile Created Successfully', count=0)

    def test_create_profile_form_validation_duplicate_email(self):
        url = reverse('create_profile')
        UserProfile.objects.create(
            first_name='Duplicate',
            surname='User',
            email='duplicate@example.com',
            phone_number='1111111111'
        )
        duplicate_data = {
            'first_name': 'Another',
            'surname': 'User',
            'email': 'duplicate@example.com',
            'phone_number': '2222222222',
        }
        response = self.client.post(url, duplicate_data)
        self.assertContains(response, 'User profile with this Email already exists.')
        self.assertContains(response, 'Profile Created Successfully', count=0)
