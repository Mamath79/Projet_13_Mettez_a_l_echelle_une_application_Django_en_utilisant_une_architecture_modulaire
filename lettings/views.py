"""
Module containing the views for the 'lettings' application.

This module defines the views for managing and displaying letting information,
including the list of all lettings and individual letting details.
"""

from django.shortcuts import render
from lettings.models import Letting


def index(request):
    """
    View function for displaying the list of all lettings.

    This view retrieves all letting objects from the database and displays them
    in a list format.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: Rendered lettings/index.html template with the list of lettings.
    """
    lettings_list = Letting.objects.all()
    context = {"lettings_list": lettings_list}
    return render(request, "lettings/index.html", context)


def letting(request, letting_id):
    """
    View function for displaying details of a specific letting.

    This view retrieves a specific letting by its ID and displays its details,
    including the title and associated address.

    Args:
        request: The HTTP request object.
        letting_id (int): The ID of the letting to display.

    Returns:
        HttpResponse: Rendered lettings/letting.html template with the letting details.

    Raises:
        Letting.DoesNotExist: If the letting with the specified ID is not found.
    """
    letting = Letting.objects.get(id=letting_id)
    context = {
        "title": letting.title,
        "address": letting.address,
    }
    return render(request, "lettings/letting.html", context)
