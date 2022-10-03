from django.urls import reverse

import pytest
from django.core.management import call_command
from rest_framework.test import APIClient

from accounts.models import User


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


@pytest.fixture()
def api_client():
    return APIClient()


@pytest.fixture()
def api_client_auth(api_client):
    password = 'password'
    email = 'example@mail.com'
    user = User(email=email)
    user.set_password(password)
    user.save()

    r = api_client.post(
        reverse('api-v1:token_obtain_pair'),
        data={'email': email, 'password': password},
    )
    assert r.status_code == 200, r.content
    assert "access" in r.json(), r.content
    token = r.json()['access']

    api_client.credentials(
        HTTP_AUTHORIZATION=f'JWT {token}'
    )
    return api_client
