import os
from celery import Celery

# 1. Tell Celery which settings file to read for configuration
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'assignments.settings')

# 2. Instantiate the Celery app variable using your project name
app = Celery('assignments')

# 3. Tell Celery to read custom variables inside your settings.py
# (Using the CELERY_ namespace prefix stops settings conflicts)
app.config_from_object('django.conf:settings', namespace='CELERY')

# 4. Tell Celery to automatically hunt for tasks.py files across your apps
app.autodiscover_tasks()
