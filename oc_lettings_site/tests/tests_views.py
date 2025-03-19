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

    @patch("django.shortcuts.render", side_effect=Exception("Simulated Template Error"))
    @patch("sentry_sdk.capture_exception")  # Vérifie que Sentry est bien appelé
    @patch("logging.getLogger")  # Vérifie que le logger Django est bien activé
    def test_index_view_error_handling(self, mock_logger, mock_sentry, mock_render):
        """
        Simule une erreur dans la vue pour tester la gestion des exceptions.
        Vérifie que :
        - La page renvoie bien une erreur 500
        - L'exception est envoyée à Sentry
        - L'erreur est bien loggée dans Django
        """
        response = self.client.get(reverse("index"))

        # Vérifie que la page affiche bien l'erreur
        self.assertEqual(response.status_code, 500)
        self.assertContains(response, "Une erreur interne est survenue.")

        # Vérifie que Sentry a bien été utilisé pour capturer l'exception
        mock_sentry.assert_called_once()

        # Vérifie que le logger a bien enregistré une erreur
        mock_logger().error.assert_called_once_with(
            "Erreur dans la vue index", exc_info=True
        )

    def test_index_view_error_direct(self):
        """
        Simule une erreur directe dans la vue index pour tester la gestion des exceptions.
        """

        with patch("django.shortcuts.render", side_effect=Exception("Erreur directe")):
            response = self.client.get(reverse("index"))
            self.assertEqual(response.status_code, 500)
            self.assertContains(response, "Une erreur interne est survenue.")
