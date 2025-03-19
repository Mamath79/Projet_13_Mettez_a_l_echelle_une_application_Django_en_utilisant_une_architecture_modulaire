import logging
import sentry_sdk
from django.shortcuts import render
from django.http import HttpResponseServerError

logger = logging.getLogger(__name__)


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
    try:
        return render(request, "index.html")
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        sentry_sdk.capture_exception(e)
        return HttpResponseServerError("Internal Server Error")
