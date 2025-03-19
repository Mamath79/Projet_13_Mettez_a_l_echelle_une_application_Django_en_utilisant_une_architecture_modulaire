from unittest.mock import patch
from django.test import TestCase, Client
from django.urls import reverse


class IndexViewTest(TestCase):
    """
    Test case for the index view of the 'oc_lettings_site' application.
    """

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
        self.assertContains(response, "Welcome to Holiday Homes")

    def test_index_view_render(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertTrue("index.html" in [t.name for t in response.templates])

    def test_index_view_error_handling(self):
        """
        Simule une erreur lors du rendu du template pour tester la gestion des exceptions.
        """
        with patch("django.shortcuts.render") as mock_render:
            mock_render.side_effect = Exception("Template error")
            response = self.client.get(reverse("index"))
            self.assertEqual(response.status_code, 500)
