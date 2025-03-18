"""
Tests unitaires pour les modèles de l'application 'profiles'.
"""

from django.test import TestCase
from django.contrib.auth.models import User
from profiles.models import Profile

class ProfileModelTest(TestCase):
    """
    Test case for the Profile model.
    """
    def setUp(self):
        """
        Set up a test Profile instance.
        """
        self.user = User.objects.create(username="testuser", password="testpassword")
        self.profile = Profile.objects.create(user=self.user, favorite_city="Paris")

    def test_profile_creation(self):
        """
        Test that the Profile instance is created correctly.
        """
        self.assertEqual(self.profile.user.username, "testuser")
        self.assertEqual(self.profile.favorite_city, "Paris")

    def test_profile_str(self):
        """
        Test that the Profile instance is represented as a string correctly.
        """
        self.assertEqual(str(self.profile), "testuser") 

    def test_profile_favorite_city(self):
        """
        Test that the Profile instance's favorite city is correctly set.
        """
        self.assertEqual(self.profile.favorite_city, "Paris")

    def test_profile_user_deletion(self):
        """
        Test that deleting a user deletes the associated profile.
        """
        self.user.delete()
        with self.assertRaises(Profile.DoesNotExist):
            Profile.objects.get(user=self.user)