# Orange County Lettings — Modular Django (P13)

> **Educational project (OpenClassrooms)**: refactor and scale a legacy Django monolith into a **modular architecture** with clear app boundaries, CI, Docker packaging, and documentation.

---

## ✨ What’s inside

- ✅ Clean split into **independent Django apps**: `oc_lettings_site`, `lettings`, `profiles`
- ✅ Central `urls.py` with **per‑app URLConfs**
- ✅ Production‑ready settings via environment variables
- ✅ **CI** (GitHub Actions) for tests & style checks
- ✅ **Dockerfile** for containerized runs
- ✅ **Sphinx docs** (Read the Docs)

> This repository is for learning/demo purposes. It is not meant for production without additional hardening.

---

## 🧱 Tech stack

- **Python 3.8+** (Django 4.x compatible)
- **Django** (templates, ORM, admin)
- **SQLite** for local runs (swap to Postgres/MySQL in prod)
- **Docker** (optional)

---

## 📦 Project structure (excerpt)

```
.
├─ oc_lettings_site/          # Project config: settings, urls, wsgi
│  ├─ settings.py
│  ├─ urls.py
│  └─ wsgi.py
├─ lettings/                  # "Lettings" bounded context
│  ├─ models.py
│  ├─ views.py
│  ├─ urls.py
│  └─ tests/
├─ profiles/                  # "Profiles" bounded context
│  ├─ models.py
│  ├─ views.py
│  ├─ urls.py
│  └─ tests/
├─ templates/                 # Shared templates
├─ docs/                      # Sphinx documentation source
├─ manage.py
├─ requirements.txt           # Python dependencies
├─ dockerfile                 # Container build recipe
└─ .env                       # Environment configuration (local)
```

---

## 🚀 Quickstart (local)

### 1) Clone & create a virtualenv

```bash
git clone https://github.com/Mamath79/Projet_13_Mettez_a_l_echelle_une_application_Django_en_utilisant_une_architecture_modulaire.git
cd Projet_13_Mettez_a_l_echelle_une_application_Django_en_utilisant_une_architecture_modulaire
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

### 2) Configure environment

Create a `.env` file in the repository root (or update the existing one):

```ini
# Django
DEBUG=True
SECRET_KEY=change-me
ALLOWED_HOSTS=127.0.0.1,localhost

# Database (SQLite by default)
# For Postgres, use individual env vars or a DATABASE_URL adapter if you add one
```

> Never commit secrets. Use a separate `.env` for production.

### 3) Run migrations & start the dev server

```bash
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```

Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/)\
Main sections: `/lettings/` and `/profiles/`.

---

## 🐳 Run with Docker (optional)

Build the image:

```bash
docker build -t oc-lettings .
```

Run the container (re-using your local `.env`):

```bash
docker run --env-file .env -p 8000:8000 \
  oc-lettings python manage.py migrate && \
  docker run --env-file .env -p 8000:8000 oc-lettings \
  python manage.py runserver 0.0.0.0:8000
```

> If you prefer **gunicorn**:
>
> ```bash
> docker run --env-file .env -p 8000:8000 oc-lettings \
>   gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:8000
> ```

For a production setup, use a multi‑service stack (reverse proxy, HTTPS, persistent DB).

---

## 🧪 Tests & quality

Run Django’s test suite:

```bash
python manage.py test
```

Optional format/lint tools you can add:

```bash
pip install black ruff
black .
ruff check .
```

---

## 🧭 Architecture notes

- **Modular monolith**: each feature lives in its own Django app (`lettings`, `profiles`) with models, views, urls and tests. This keeps boundaries clear and makes scaling (or extracting services) easier.
- **Settings via env**: configuration is read from environment variables so you can vary behavior per environment (dev/stage/prod) without touching code.
- **URLs**: project‑level `oc_lettings_site/urls.py` includes per‑app `urls.py`. Templates are namespaced accordingly.

---

## 📚 Documentation

- Project documentation is authored with **Sphinx** in `docs/`.\
  If you publish it on Read the Docs, link it here.

Build docs locally:

```bash
pip install -r docs/requirements.txt  # if present
(cd docs && make html)
```

---

## 🛳️ Deployment (example checklist)

- Switch to **PostgreSQL** and set proper credentials
- Set `DEBUG=False`, `ALLOWED_HOSTS=<your-domain>`
- Use a WSGI server: `gunicorn oc_lettings_site.wsgi:application`
- Serve via a reverse proxy (Nginx/Traefik) with HTTPS
- Add observability (Sentry, logs) and a process manager (systemd or Docker orchestrator)

---

## 📄 License

This repository is provided for **educational purposes** (OpenClassrooms). If you intend to reuse/redistribute, add a license file (e.g., MIT) and update this section.

---

## 👤 Author

**Mathieu Vieillefont**\
LinkedIn: [https://www.linkedin.com/in/mathieu-vieillefont/](https://www.linkedin.com/in/mathieu-vieillefont/)

