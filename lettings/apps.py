"""
Module for configuring the 'lettings' application.

This module contains the configuration class for the 'lettings' application,
which is responsible for setting the application's name attribute and other configurations.
"""
from django.apps import AppConfig


class LettingsConfig(AppConfig):
    """
    Configuration class for the 'lettings' application.

    This class is responsible for configuring the 'lettings' application
    and setting its name attribute.

    Attributes:
        name (str): The name of the application.
    """
    name = "lettings"
