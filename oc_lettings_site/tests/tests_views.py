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

    # @patch("django.shortcuts.render", side_effect=Exception("Simulated Template Error"))
    # @patch("sentry_sdk.capture_exception")
    # @patch("logging.getLogger")
    # def test_index_view_error_handling(self, mock_logger, mock_sentry, mock_render):
    #     """
    #     Simulates an error in the view to test exception handling.
    #     Verifies that:
    #     - The page returns a 500 error
    #     - The exception is sent to Sentry
    #     - The error is logged in Django
    #     """
    #     response = self.client.get(reverse("index"))

    #     # Vérifie que la page affiche bien l'erreur
    #     self.assertEqual(response.status_code, 500)
    #     self.assertEqual(response["Content-Type"], "text/plain")
    #     self.assertContains(response, "Une erreur interne est survenue.")

    #     # Vérifie que Sentry capture bien l'exception
    #     mock_sentry.assert_called_once()

    #     # Vérifie que le logger a bien enregistré une erreur
    #     mock_logger().error.assert_called_once_with(
    #         "Erreur dans la vue index", exc_info=True
    #     )

    # def test_index_view_error_direct(self):
    #     """
    #     Also simulates a direct error in the index view to test exception handling.
    #     """
    #     with patch("django.shortcuts.render", side_effect=Exception("Erreur directe")):
    #         response = self.client.get(reverse("index"))
    #         self.assertEqual(response.status_code, 500)
    #         self.assertEqual(response["Content-Type"], "text/plain")
    #         self.assertContains(response, "Une erreur interne est survenue.")