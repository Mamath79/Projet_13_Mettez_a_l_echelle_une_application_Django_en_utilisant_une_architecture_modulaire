"""
Module for configuring the 'profiles' application.

This module contains the configuration class for the 'profiles' application,
which is responsible for setting the application's name attribute and other configurations.
"""
from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    """
    Configuration class for the 'profiles' application.

    This class is responsible for configuring the 'profiles' application
    and setting its name attribute.

    Attributes:
        name (str): The name of the application.
    """
    name = "profiles"
