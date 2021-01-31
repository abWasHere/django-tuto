# django-tuto personal notes

## create a virtual environment first !

`python3 -m venv my_vitrual_env`

option with virtualenv : `virtualenv -p python3 my_virtual_env`

`source my_virtual_env/bin/activate` => activation (the name of the env will appear in front of the prompt)

`deactivate`

## install django in the virtual env

`python -m pip install Django`

`pip freeze`
=> check all the installed package in this virtual env

## initiating project

`django-admin startproject my_project`
=> creates a subfolder with the main app of the project + manage.py

- my_project (= subfolder)
  - my_project (= main app)
  - manage.py (= root of the django project)

`django-admin startproject my_project .`
=> does not create a subfolder

- my_project (= main app)
- manage.py

## start server

`python manage.py runserver`

## urls.py

looks at the URL request
decides which function to fire in views.py
in settings.py : ROOT_URLCONF indicates the file where the URLs are defined (URLs + corresponding views)

### dynamic URL

`path("products/<int:my_id>/", dynamic_lookup_view, name="product")`

handle page_not_found :
`from django.shortcuts import render, get_object_or_404`
or
`from django.http import Http404`

## views.py

functions that will : send either a response or an html template to the browser
in settings.py : import views to associate them with URLs

## templates

= actual django-html file (page rendered by the view function)
WARNING : templates folder has to be set in the settings.py file
TEMPLATES = [... DIRS : 'templates', ...]

#### template engine

=> you want to use a base layout for example, or have a navbar or footer on every page without repeating the code.
Be careful ! When using a layout template : to fill the content block, use the same block name in the template file.

#### rendering context in a template

in views.py, in my def whatever_view :
if my_context = {my_context_key : my_val}

in my django-html file :
write {{my_context_key}} will display my_val

## django apps

Each app is a component.
Built in apps : admin, auth, contenttypes, sessions, messages, staticfiles

### admin app

http://127.0.0.1:8000/admin/login/?next=/admin/

`python manage.py createsuperuser`
=> this user can log in the admin site and has all permissions; this user is in the DB

### create a new app in the root directory

`python manage.py startapp my_secondary_app`

- root project directory
  - manage.py (automatically created)
  - template (automatically created)
  - main app (automatically created)
    - urls.py
    - settings/
  - app 2
    - **init.py**
    - apps.py
    - models.py
    - tests.py
    - urls.py
    - views.py
    - templates/
  - app 3
    - (idem app 2)
  - etc...

##### then add you app to setting.py in INSTALLED_APPS list

## django models

Commands to run everytime a db model is modified (in a models.py):
`python manage.py makemigrations` => look for changes (migrations)
`python manage.py migrate` => apply all migrations

### models

### create model Objects in the Python shell

=> Faster way to create objects instead of navigating into the Admin site

`python manage.py shell`
=> opens a Python interpreter

`from my_products_app.models import Product`
=> import the Product model that I created in the app my_products_app

`Product.ojects.all()` = QuerySet of Product objects

`Product.objects.create(title='whatever', desc='something')`
