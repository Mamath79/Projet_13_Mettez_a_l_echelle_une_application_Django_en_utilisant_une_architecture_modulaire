"""
Module for registering the 'lettings' application's models with the Django admin site.

This module registers the Letting and Address models to be manageable through the
Django admin interface.
"""

from django.contrib import admin
from .models import Letting, Address

admin.site.register(Letting)
admin.site.register(Address)
