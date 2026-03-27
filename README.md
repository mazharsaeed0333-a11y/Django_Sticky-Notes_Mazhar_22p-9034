# Sticky Notes (Django)

Web Engineering Assignment #2 — Sticky Notes App.

## Setup (Windows / PowerShell)

From the project root (this folder):

```powershell
python -m venv .venv
.\.venv\Scripts\python -m pip install -r requirements.txt
cd sticky_project
..\.venv\Scripts\python manage.py migrate
..\.venv\Scripts\python manage.py runserver
```

## URLs

- `http://127.0.0.1:8000/register/` — Register
- `http://127.0.0.1:8000/login/` — Login
- `http://127.0.0.1:8000/notes/` — Note list (home)
- `http://127.0.0.1:8000/notes/new/` — Create note
