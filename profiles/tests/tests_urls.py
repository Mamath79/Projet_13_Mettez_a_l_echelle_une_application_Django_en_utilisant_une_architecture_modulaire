"""
Tests unitaires pour les URLs de l'application 'profiles'.
"""

from django.test import SimpleTestCase
from django.urls import reverse, resolve
from profiles.views import profile

class TestUrls(SimpleTestCase):
    """
    Test case for the URLs in the profiles application.
    """

    def test_profile_url_is_resolved(self):
        """
        Test that the profile URL resolves correctly.
        """
        url = reverse('profiles:profile', args=['testuser'])
        self.assertEqual(resolve(url).func, profile)
