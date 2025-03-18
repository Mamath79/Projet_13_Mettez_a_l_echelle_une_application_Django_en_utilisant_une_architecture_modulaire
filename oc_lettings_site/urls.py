"""
URL configuration for the 'oc_lettings_site' project.

This module defines the main URL patterns for the entire project, including:
- The main index page
- The lettings application URLs
- The profiles application URLs
- The Django admin interface

The URLs are organized using namespaces to avoid naming conflicts between
different applications.
"""

from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("lettings/", include("lettings.urls", namespace="lettings")),
    path("profiles/", include("profiles.urls", namespace="profiles")),
    path("admin/", admin.site.urls),
]
