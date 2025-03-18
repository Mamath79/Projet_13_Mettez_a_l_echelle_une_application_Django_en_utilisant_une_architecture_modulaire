"""
Module for registering the 'profiles' application's models with the Django admin site.

This module registers the Profile model to be manageable through the
Django admin interface.
"""

from django.contrib import admin
from .models import Profile

admin.site.register(Profile)
