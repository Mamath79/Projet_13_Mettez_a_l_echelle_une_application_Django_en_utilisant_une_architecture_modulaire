"""
URL configuration for the 'lettings' application.

This module defines the URL patterns for the lettings application, which handles
the routing for:
- The list of all lettings (index page)
- Individual letting details pages

The URLs are namespaced under 'lettings' to avoid conflicts with other applications.
"""

from django.urls import path
from . import views

app_name = "lettings"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:letting_id>/", views.letting, name="letting"),
]
