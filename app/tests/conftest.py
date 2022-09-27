import pytest
from django.core.management import call_command
# from rest_framework.test import APIClient


@pytest.fixture(autouse=True, scope="function")
def enable_db_for_all_tests(db):
    """
    access to db
    """


@pytest.fixture(autouse=True, scope="session")
def load_fixtures(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        fixtures = (
            'sourсes.json',
            'rates.json',
            'contactus.json'
        )
        for fixture in fixtures:
            call_command('loaddata', f'app/tests/fixtures/{fixture}')
