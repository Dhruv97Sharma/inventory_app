# Django inventory app with APIs

Building an inventory app with django and drf in the backend.

## Features

- Django 3.0+
- Uses [venv](https://docs.python.org/3/library/venv.html) - the officially recommended Python packaging tool from Python.org.
- Development, Staging and Production settings with [django-configurations](https://django-configurations.readthedocs.org).
- Get value insight and debug information while on Development with [django-debug-toolbar](https://django-debug-toolbar.readthedocs.org).
- Collection of custom extensions with [django-extensions](http://django-extensions.readthedocs.org).
- HTTPS and other security related settings on Staging and Production.
- Procfile for running gunicorn with New Relic's Python agent.
- PostgreSQL database support with psycopg2.
- Using Neon Tech PostgreSQL managed DB [neon.tech](https://neon.tech/docs/introduction).


## How to install

```bash
# Clone the repository
git clone https://github.com/dhruv97sharma/django-inventory-app-apis.git
cd django-inventory-app-apis

# Create a virtual environment
python3 -m venv ./env
source ./venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Environment variables

Since I am using neon tech postgres managed DB for this example, this is how you would need to setup the database url variable in an .env file. Use the .env.local file template to fill all the config values of the database in your .env file.


## Deployment

It is possible to deploy to render.com, railway.app or to your own server.


## License

The MIT License (MIT)
