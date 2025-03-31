Usage
=====

Once the project is installed and running, you can use the application in the following ways:

Homepage
--------
Visit `http://127.0.0.1:8000/` to access the homepage. This page serves as the entry point to the application.

Profiles
--------
- Click on the **Profiles** button from the homepage.
- View the list of user profiles.
- Click on a profile to see detailed information.

Lettings
--------
- Click on the **Lettings** button from the homepage.
- View the list of available rental properties.
- Click on a letting to view detailed address information.

Admin Panel
-----------
- Visit `http://127.0.0.1:8000/admin/`
- Log in using Django superuser credentials.
- Manage users, profiles, and lettings directly from the admin interface.

Static Files and UI
-------------------
The application includes custom CSS and JS located in the `static/` directory. These assets are automatically collected and served when you run the `collectstatic` command and serve the application via Django or Docker.

Error Monitoring
----------------
If you have configured a `SENTRY_DSN` in your `.env`, Sentry will automatically capture unhandled exceptions and errors in production mode.

This setup allows both developers and users to interact with the project in a clear and user-friendly manner.

