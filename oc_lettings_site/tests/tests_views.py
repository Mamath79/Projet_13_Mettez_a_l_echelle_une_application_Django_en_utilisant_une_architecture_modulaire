from unittest.mock import patch
from django.test import TestCase, Client
from django.urls import reverse


class IndexViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_view_status_code(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)

    def test_index_view_template(self):
        response = self.client.get(reverse("index"))
        self.assertTemplateUsed(response, "index.html")

    def test_index_view_content(self):
        response = self.client.get(reverse("index"))
        self.assertContains(response, "test changement nom v4")

    def test_index_view_render(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertTrue("index.html" in [t.name for t in response.templates])

    @patch("sentry_sdk.capture_exception")
    @patch("oc_lettings_site.views.render", side_effect=Exception("Simulated Template Error"))
    def test_index_view_error_handling(self, mock_render, mock_sentry):
        response = self.client.get(reverse("index"))

        self.assertEqual(response.status_code, 500)
        self.assertIn(b"Internal Server Error", response.content)
        mock_sentry.assert_called_once()
