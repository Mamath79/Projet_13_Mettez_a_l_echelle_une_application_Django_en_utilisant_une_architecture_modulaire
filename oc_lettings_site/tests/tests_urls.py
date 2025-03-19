"""
Unit tests for the URLs of the 'oc_lettings_site' application.
"""

from django.test import SimpleTestCase
from django.urls import reverse, resolve
from oc_lettings_site.views import index


class TestUrls(SimpleTestCase):
    """
    Test case for the URLs of the 'oc_lettings_site' application.
    """

    def test_index_url_resolves(self):
        """
        Test that the index URL resolves to the correct view.
        """
        url = reverse("index")
        self.assertEqual(resolve(url).func, index)
