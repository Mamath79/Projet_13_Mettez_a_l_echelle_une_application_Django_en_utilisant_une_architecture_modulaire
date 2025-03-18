"""
Tests unitaires pour les vues de l'application 'profiles'.
"""

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from profiles.models import Profile

class ProfileViewTest(TestCase):
    """
    Test case for the Profile view.
    """

    def setUp(self):
        """
        Set up a test client and a test user with a profile.
        """
        self.client = Client()
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.profile = Profile.objects.create(user=self.user, favorite_city="Paris")

    def test_profile_view_status_code(self):
        """
        Test that the profile view returns a 200 status code.
        """
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get(reverse('profiles:profile', args=[self.user.username]))
        self.assertEqual(response.status_code, 200)

    def test_profile_view_template(self):
        """
        Test that the profile view uses the correct template.
        """
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get(reverse('profiles:profile', args=[self.user.username]))
        self.assertTemplateUsed(response, 'profiles/profile.html')

    def test_profile_view_context(self):
        """
        Test that the profile view provides the correct context data.
        """
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get(reverse('profiles:profile', args=[self.user.username]))
        self.assertEqual(response.context['profile'].favorite_city, "Paris")
