"""
Module containing the views for the 'lettings' application.

This module defines the views for managing and displaying letting information,
including the list of all lettings and individual letting details.
"""

from lettings.models import Letting
from django.shortcuts import render
from django.http import Http404
import sentry_sdk


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
    try:
        lettings_list = Letting.objects.all()
        context = {"lettings_list": lettings_list}
        return render(request, "lettings/index.html", context)
    except Exception as e:
        sentry_sdk.capture_exception(e)
        raise


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
    try:
        letting = Letting.objects.get(id=letting_id)
        context = {
            "title": letting.title,
            "address": letting.address,
        }
        return render(request, "lettings/letting.html", context)
    except Letting.DoesNotExist:
        sentry_sdk.capture_message(f"Letting not found: {letting_id}", level="error")
        raise Http404("Letting does not exist")
    except Exception as e:
        sentry_sdk.capture_exception(e)
        raise
