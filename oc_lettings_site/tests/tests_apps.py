from django.test import TestCase
from django.apps import apps
from oc_lettings_site.apps import OCLettingsSiteConfig


class OCLettingsSiteConfigTest(TestCase):
    """
    Test case for the OCLettingsSiteConfig class.

    This test case ensures that the OCLettingsSiteConfig class is correctly configured
    and that the application name is set properly.
    """

    def test_apps(self):
        """
        Test that the OCLettingsSiteConfig class is correctly configured.

        This test checks that the OCLettingsSiteConfig class is registered with the
        correct application name.
        """
        self.assertEqual(OCLettingsSiteConfig.name, "oc_lettings_site")
        self.assertEqual(apps.get_app_config("oc_lettings_site").name, "oc_lettings_site")
