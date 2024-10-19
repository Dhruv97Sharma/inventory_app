import dj_database_url
import os
# Replace the DATABASES section of your settings.py with this

DATABASE_URL = os.getenv('DATABASE_URL')

DATABASES = {
  'default': dj_database_url.config(
        engine='django.db.backends.postgresql',
        default=DATABASE_URL,
        conn_max_age=10000,
        conn_health_checks=True
    )
}