Development
===========

If you want to contribute or further develop the project, here are a few helpful notes:

Code Style:
-----------
- The project follows **PEP8** coding conventions.
- Use `flake8` to verify linting before committing.
- Format your code using `black` or `autopep8`.

Architecture:
-------------
- Modular Django structure with apps: `lettings`, `profiles`, and `oc_lettings_site`.
- Views are tested and documented.
- Each app contains its own models, URLs, views, and tests.

Testing:
--------
- Unit and integration tests are in `*/tests` directories.
- Use `pytest` for consistent test execution.
- CI ensures coverage above 80%.

Containers:
-----------
- A `Dockerfile` is available for building a production-ready image.
- The image is published to Docker Hub and used by Render for deployment.

CI/CD:
------
- GitHub Actions manages automated testing, image publishing, and deployment.
- Only commits to `master` trigger deployment.

Documentation:
--------------
- Built with **Sphinx** in the `/docs` folder.
- To build the HTML docs:

  .. code-block:: console

     cd docs
     make html

- Open the result with:

  .. code-block:: console

     open _build/html/index.html
