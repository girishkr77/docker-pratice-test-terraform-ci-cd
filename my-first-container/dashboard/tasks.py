from celery import shared_task
import time

@shared_task
def backgroung_worker():
    time.sleep(3)
    print('shared task is completed')