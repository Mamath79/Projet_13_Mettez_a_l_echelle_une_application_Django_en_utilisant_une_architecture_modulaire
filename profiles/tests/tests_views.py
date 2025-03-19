"""
Unit tests for the views of the 'profiles' application.
"""

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from profiles.models import Profile


class ProfileViewTest(TestCase):
    """
    Test case for the views of the 'profiles' application.
    """

    def setUp(self):
        """
        Set up a test client and create test users with profiles.
        """
        self.client = Client()
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.profile = Profile.objects.create(user=self.user, favorite_city="Paris")

    def test_profiles_index_view_status_code(self):
        """
        Test that the profile index view returns a 200 status code.
        """
        response = self.client.get(reverse("profiles:index"))
        self.assertEqual(response.status_code, 200)

    def test_profiles_index_view_template(self):
        """
        Test that the profile index view uses the correct template.
        """
        response = self.client.get(reverse("profiles:index"))
        self.assertTemplateUsed(response, "profiles/index.html")

    def test_profiles_index_view_content(self):
        """
        Test that the profile index view contains the expected content.
        """
        response = self.client.get(reverse("profiles:index"))
        self.assertContains(response, "testuser")

    def test_profile_view_status_code(self):
        """
        Test that the profile detail view returns a 200 status code.
        """
        response = self.client.get(reverse("profiles:profile", args=[self.user.username]))
        self.assertEqual(response.status_code, 200)

    def test_profile_view_template(self):
        """
        Test that the profile detail view uses the correct template.
        """
        response = self.client.get(reverse("profiles:profile", args=[self.user.username]))
        self.assertTemplateUsed(response, "profiles/profile.html")

    def test_profile_view_context(self):
        """
        Test that the profile view provides the correct context data.
        """
        response = self.client.get(reverse("profiles:profile", args=[self.user.username]))
        self.assertEqual(response.context["profile"].favorite_city, "Paris")

    def test_profile_view_not_found(self):
        """
        Test that the profile view returns a 404 status code for a non-existent user.
        """
        response = self.client.get(reverse("profiles:profile", args=["unknown_user"]))
        self.assertEqual(response.status_code, 404)
