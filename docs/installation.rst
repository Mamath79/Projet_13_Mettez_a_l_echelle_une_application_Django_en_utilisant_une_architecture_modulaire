AA Installation
============

Follow these steps to install and run the Python-OC-Lettings application locally.

Prerequisites
-------------

- Python 3.10+
- pip
- Git
- Docker (optional, for containerized setup)

Clone the repository
---------------------

.. code-block:: console

   git clone https://github.com/Mamath79/Projet_13_Mettez_a_l_echelle_une_application_\
   Django_en_utilisant_une_architecture_modulaire.git


.. code:: bash

   cd your-repo


Create and activate a virtual environment
-----------------------------------------

.. code-block:: bash

   python -m venv venv
   source venv/bin/activate       # On Linux and Mac 
   source venv\Scripts\activate   # On Windows

Install dependencies
--------------------

.. code-block:: bash

   pip install -r requirements.txt

Set environment variables
-------------------------

Create a ``.env`` file at the root of the project and configure it as follows:

.. code-block:: ini

   DEBUG=True
   SECRET_KEY=your-secret-key
   ALLOWED_HOSTS=127.0.0.1,localhost
   SENTRY_DSN=your-sentry-dsn

Apply migrations and collect static files
-----------------------------------------

.. code-block:: bash

   python manage.py migrate
   python manage.py collectstatic --noinput

Run the development server
--------------------------

.. code-block:: bash

   python manage.py runserver

The application will be available at http://127.0.0.1:8000.

Run with Docker (alternative)
-----------------------------

Build and run the Docker container:

.. code-block:: bash

   docker build -t python-oc-lettings .
   docker run --env-file .env -p 8000:8000 python-oc-lettings

The app will also be available at http://127.0.0.1:8000.

