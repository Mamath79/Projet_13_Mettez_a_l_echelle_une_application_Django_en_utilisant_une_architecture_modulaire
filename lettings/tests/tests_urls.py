"""
Unit tests for the 'lettings' application URLs.
"""

from django.test import SimpleTestCase
from django.urls import resolve, reverse
from lettings.views import index, letting


class LettingsURLsTest(SimpleTestCase):
    """
    Test case for the URL configuration of the 'lettings' application.
    """

    def test_index_url_resolves(self):
        """
        Test that the lettings index URL resolves correctly.
        """
        url = reverse("lettings:index")
        self.assertEqual(resolve(url).func, index)

    def test_letting_url_resolves(self):
        """
        Test that the letting detail URL resolves correctly.
        """
        url = reverse("lettings:letting", args=[1])
        self.assertEqual(resolve(url).func, letting)
