## Orange County Lettings - Python Django Project

This is a Django-based web application for managing lettings and user profiles, developed as part of the OpenClassrooms Python Developer path.

---

### Contents

- [Features](#features)
- [Development Setup](#development-setup)
  - [macOS / Linux](#macos--linux)
  - [Windows](#windows)
- [Linting](#linting)
- [Testing](#testing)
- [Database](#database)
- [Admin Panel](#admin-panel)

---

## Features

- Index page with access to lettings and user profiles
- Lettings and profiles management
- Admin interface
- Full CI/CD with Docker & GitHub Actions
- Deployment to Render

---

## Development Setup

### Prerequisites

- GitHub account with repository access
- Git CLI
- SQLite3 CLI
- Python 3.6+

---

### macOS / Linux

#### Clone the repository

```bash
cd /path/to/put/project/in
git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git
cd Python-OC-Lettings-FR
```

#### Create and activate virtual environment

```bash
python -m venv venv
source venv/bin/activate
```

If `python3-venv` is missing:
```bash
sudo apt-get install python3-venv
```

Check versions:
```bash
which python
python --version
which pip
```
To deactivate:
```bash
deactivate
```

#### Run the server

```bash
pip install -r requirements.txt
python manage.py runserver
```
Visit: `http://localhost:8000`

---

### Windows (PowerShell)

```powershell
cd /path/to/put/project/in
git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git
cd Python-OC-Lettings-FR
python -m venv venv
.\venv\Scripts\Activate.ps1
```

Check versions:
```powershell
(Get-Command python).Path
python --version
(Get-Command pip).Path
```

---

## Linting

```bash
flake8
```

---

## Testing

```bash
pytest
```

---

## Database

```bash
sqlite3
.open oc-lettings-site.sqlite3
.tables
pragma table_info(Python-OC-Lettings-FR_profile);
select user_id, favorite_city from Python-OC-Lettings-FR_profile where favorite_city like 'B%';
.quit
```

---

## Admin Panel

Visit: `http://localhost:8000/admin`

Use:
- **Username**: `admin`
- **Password**: `Abc1234!`

---

## Documentation

Online documentation is available at: https://projet-13-mettez-a-l-echelle-une-application-django.readthedocs.io/en/latest/index.html
---