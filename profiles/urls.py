"""
URL configuration for the 'profiles' application.

This module defines the URL patterns for the profiles application, which handles
the routing for:
- The list of all user profiles (index page)
- Individual user profile pages

The URLs are namespaced under 'profiles' to avoid conflicts with other applications.
"""

from django.urls import path
from . import views

app_name = "profiles"

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:username>/", views.profile, name="profile"),
]
