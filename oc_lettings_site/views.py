"""
Module containing the views for the main 'oc_lettings_site' application.

This module defines the core views for the main application, including the index page
and views for managing profiles and lettings.
"""

from django.shortcuts import render


def index(request):
    """
    View function for the main index page.

    This view renders the main landing page of the application, which serves as the
    entry point for users to access different sections of the site.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: Rendered index.html template.
    """
    return render(request, "index.html")
