# Utilisation d'une image officielle Python comme base
FROM python:3.10

# Définition du répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers du projet dans le conteneur
COPY . /app/
COPY .env /app/.env  

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Collecter les fichiers statiques
RUN python manage.py collectstatic --noinput

# Exposer le port sur lequel Django tourne
EXPOSE 8000

# Utilisation de "env" au lieu de "source"
CMD ["bash", "-c", "export $(grep -v '^#' /app/.env | xargs) && gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:8000"]


