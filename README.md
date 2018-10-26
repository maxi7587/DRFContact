# DRFContact

Django REST Framework app for storing contact data.

## How to explore DRFContact app using the browsable API

You can quickly *explore DRFContacts app* creating, updating or deleting objects *using Django REST Framework Browsable API*.

- Clone the repository: `git clone https://github.com/maxi7587/DRFContact.git`
- Go into the project folder: `cd DRFContact`
- Create a virtualenv: `virtualenv env`
- Install requirements: `pip install requirements.txt`
- Create migrations: `python manage.py makemigrations`
- Run migrations: `python manage.py migrate`
- Start server: `python manage.py runserver`
- Open the following URL in the browser: `127.0.0.1:8000` (or the one shown in console)

## Include DRCOntact app in an existing project

To *include DRFContact app in your existing Django REST Framework project*:

- Copy the folder called DRFContact (inside DRFContact project) to your project's app's folder
- Add the app to the `INSTALLED_APPS` list in your project's settings.py file
- Create migrations: `python manage.py makemigrations`
- Run migrations: `python manage.py migrate`

That's all, you can start including DRFContact resources in your models  to store contact data such as address, phone, mail, website, social media, etc.

Hope it's useful. *Recomendations and PR's are welcome!*
