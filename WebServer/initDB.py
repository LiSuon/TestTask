import os
import django
import time

time.sleep(15)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WebServer.settings')

django.setup()

from django.contrib.auth import get_user_model

from django.core.management import call_command

def run_migrations():

    try:
        print("Running makemigrations...")
        call_command('makemigrations')
        print("Running migrate...")
        call_command('migrate')
        print("Migrations applied successfully.")
    except Exception as e:
        print(f"An error occurred during migrations: {e}")

def run_server():
    try:
        call_command("runserver", "0.0.0.0:8000")
    except:
        print("Error")

if __name__ == "__main__":
    run_migrations()
    run_server()
