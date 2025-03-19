"""
Module containing the views for the 'profiles' application.

This module defines the views for managing and displaying user profiles,
including the list of all profiles and individual profile details.
"""

from django.shortcuts import render, get_object_or_404
from profiles.models import Profile


def index(request):
    """
    View function for displaying the list of all user profiles.

    This view retrieves all profile objects from the database and displays them
    in a list format.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: Rendered profiles/index.html template with the list of profiles.
    """
    profiles_list = Profile.objects.all()
    context = {"profiles_list": profiles_list}
    return render(request, "profiles/index.html", context)


def profile(request, username):
    """
    View function for displaying details of a specific user profile.

    If the profile does not exist, return a 404 error.
    """
    profile = get_object_or_404(Profile, user__username=username)
    context = {"profile": profile}
    return render(request, "profiles/profile.html", context)
