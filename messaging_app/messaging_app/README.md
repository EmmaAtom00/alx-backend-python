# ✅ **Step 1 — Create a New Django Project**

Make sure you have **Python** installed (3.9+ recommended).

### 1. Create a virtual environment (recommended)

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**macOS / Linux**

```bash
source venv/bin/activate
```

### 2. Install Django

```bash
pip install django
```

### 3. Create the project

```bash
django-admin startproject messaging_app
```

This generates a folder structure:

```
messaging_app/
    manage.py
    messaging_app/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```

---

# ✅ **Step 2 — Install Django REST Framework**

Inside your virtual environment, install DRF:

```bash
pip install djangorestframework
```

Then open:

```
messaging_app/messaging_app/settings.py
```

Find the `INSTALLED_APPS` list and add:

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```

(Keep the existing apps—just add `'rest_framework',`.)

---

# ✅ **Step 3 — Create the Messaging App**

Navigate into the project folder:

```bash
cd messaging_app
```

Create the app:

```bash
python manage.py startapp chats
```

Your project structure now looks like:

```
messaging_app/
    manage.py
    messaging_app/
        settings.py
        ...
    chats/
        admin.py
        apps.py
        models.py
        views.py
        tests.py
```

Then register the new app in **settings.py**:

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'chats',
]
```

---


It looks like whatever tool or template you’re using requires **additional REST Framework settings** (permissions + authentication) that you haven’t added yet.

Here’s how to fix it.

---

# ✅ **Fix: Add REST Framework Settings in `settings.py`**

Open:

```
messaging_app/messaging_app/settings.py
```

Add this block at the **bottom of the file** (or anywhere after `INSTALLED_APPS`):

```python
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],

    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],
}
```

---

# 📌 Make Sure These Are Also Included

### 1. **rest_framework in INSTALLED_APPS**

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'chats',
]
```

---

# 🔍 Why You Were Getting the Error

The error message says your settings file is missing:

* `"rest_framework.permissions.IsAuthenticated"`
* `"DEFAULT_AUTHENTICATION_CLASSES"`
* `"rest_framework.authentication.SessionAuthentication"`

These all belong inside the `REST_FRAMEWORK` configuration dictionary.

Once you add that block, Django REST Framework will know:

### ✔️ all API views require authentication

### ✔️ use session authentication by default

### ✔️ permissions are enforced

---

# 🎉 After Fixing It

Run:

```bash
python manage.py runserver
```

If no errors appear, your configuration is correct.

---
