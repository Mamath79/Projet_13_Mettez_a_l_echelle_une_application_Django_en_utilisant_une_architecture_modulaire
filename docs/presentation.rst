Presentation
============

AAA Python-OC-Lettings is a Django-based web application developed as part of a learning project. The application simulates a vacation rental platform, allowing users to explore profiles and listings of lettings.

The goal of this project is to apply best practices in modular Django architecture, containerization, testing, continuous integration/deployment (CI/CD), and documentation.

This application is structured into several Django apps:

- **oc_lettings_site**: The main Django project, responsible for global settings, routing, and the homepage.
- **lettings**: Manages rental listings, with models such as Letting and Address.
- **profiles**: Manages user profiles, including associations with Django's built-in User model.

Key technologies used:

- **Django** for web framework
- **Docker** for containerization
- **GitHub Actions** for CI/CD
- **Render** for deployment
- **Sentry** for error monitoring
- **Pytest & Coverage** for testing and test coverage analysis

This documentation provides everything you need to understand, install, use, test, deploy, and contribute to the project.

