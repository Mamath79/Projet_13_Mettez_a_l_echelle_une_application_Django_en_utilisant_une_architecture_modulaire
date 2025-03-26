"""
Unit tests for the URLs of the 'oc_lettings_site' application.
"""

from django.test import SimpleTestCase, TestCase
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


class TestSentryDebugView(TestCase):
    def test_sentry_debug_view(self):
        """
        Test that the sentry-debug view returns a 200 status code
        and uses the expected template (500.html).
        """
        response = self.client.get("/sentry-debug/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "500.html")
