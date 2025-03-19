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

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.shortcuts import render

from . import views
import logging
import sentry_sdk

logger = logging.getLogger(__name__)


def example_view(request):
    """
    Example view function to demonstrate error logging.

    This view function attempts to perform a division by zero operation,
    which will raise a ZeroDivisionError. The error is caught and logged
    using the logger, and an error page is rendered.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: Rendered error.html template with an error message.
    """
    try:
        1 / 0
    except ZeroDivisionError as e:
        logger.error("Une division par zéro a été détectée !", exc_info=True)
        sentry_sdk.capture_exception(e)
        return render(request, "500.html")


urlpatterns = [
    path("", views.index, name="index"),
    path("lettings/", include("lettings.urls", namespace="lettings")),
    path("profiles/", include("profiles.urls", namespace="profiles")),
    path("admin/", admin.site.urls),
    path("sentry-debug/", example_view),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0]
    )
