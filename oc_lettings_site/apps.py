"""
Module for configuring the 'oc_lettings_site' application.

This module contains the configuration class for the 'oc_lettings_site' application,
which is responsible for setting the application's name attribute and other configurations.
"""
from django.apps import AppConfig


class OCLettingsSiteConfig(AppConfig):
    """
    Configuration class for the 'oc_lettings_site' application.

    This class is responsible for configuring the 'oc_lettings_site' application
    and setting its name attribute.

    Attributes:
        name (str): The name of the application.
    """
    name = "oc_lettings_site"
