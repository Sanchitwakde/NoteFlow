# NoteFlow

NoteFlow is a Django notes app backed by MySQL. Users can register, log in, create notes, edit notes, delete notes, pin important notes, search by title or content, and filter notes by category.

## Tech Stack

- Python
- Django 4.2
- MySQL
- HTML, CSS, and JavaScript
- PyMySQL fallback for environments where `mysqlclient` is unavailable

## Project Structure

```text
NoteFlow/
+-- README.md
+-- requirements.txt
+-- setup_mysql.sql
+-- src/
|   +-- manage.py
|   +-- notes_project/
|   |   +-- __init__.py
|   |   +-- settings.py
|   |   +-- urls.py
|   |   +-- wsgi.py
|   +-- notes_app/
|       +-- forms.py
|       +-- models.py
|       +-- urls.py
|       +-- views.py
|       +-- migrations/
|       +-- templates/
|           +-- notes_app/
+-- venv/
```

## Requirements

- Python 3.10 or newer
- MySQL 8.0 or compatible
- pip

## Setup

1. Create and activate a virtual environment:

```powershell
python -m venv venv
venv\Scripts\activate
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Create the MySQL database:

```powershell
mysql -u root -p < setup_mysql.sql
```

4. Check the database configuration in `src/notes_project/settings.py`.

The current default configuration is:

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "notes_db",
        "USER": "root",
        "PASSWORD": "12345678",
        "HOST": "localhost",
        "PORT": "3306",
    }
}
```

Update those values if your MySQL username or password is different.

5. Run migrations:

```powershell
python src\manage.py migrate
```

6. Start the development server:

```powershell
python src\manage.py runserver
```

Open the app at:

```text
http://127.0.0.1:8000/
```

## Useful Commands

Run Django checks:

```powershell
python src\manage.py check
```

Create an admin user:

```powershell
python src\manage.py createsuperuser
```

Open the Django admin:

```text
http://127.0.0.1:8000/admin/
```

## Features

- User registration and login
- Per-user notes
- Create, read, update, and delete notes
- Pin notes to the top
- Search notes by title or content
- Filter notes by category
- Dashboard counts for total, pinned, and shown notes
- AJAX pin toggle without a full page refresh

## Routes

| Route | Description |
| --- | --- |
| `/` | Notes dashboard |
| `/register/` | Register a new account |
| `/login/` | Log in |
| `/logout/` | Log out |
| `/notes/create/` | Create a note |
| `/notes/<id>/` | View a note |
| `/notes/<id>/edit/` | Edit a note |
| `/notes/<id>/delete/` | Delete a note |
| `/notes/<id>/pin/` | Toggle pinned status |
| `/admin/` | Django admin |

## Troubleshooting

If `venv\Scripts\python.exe` points to a missing Python installation, recreate the virtual environment:

```powershell
Remove-Item -Recurse -Force venv
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

If Django reports `Error loading MySQLdb module`, install the project dependencies again:

```powershell
pip install -r requirements.txt
```

The app includes a PyMySQL fallback, so it can run even when the compiled `mysqlclient` package is not available.

If MySQL refuses the connection, confirm that:

- MySQL is running
- `notes_db` exists
- the username and password in `src/notes_project/settings.py` are correct

## Production Notes

Before deploying this app:

- Set `DEBUG = False`
- Move `SECRET_KEY` into an environment variable
- Replace `ALLOWED_HOSTS = ["*"]` with the real hostnames
- Move database credentials out of source code
- Configure static file serving
