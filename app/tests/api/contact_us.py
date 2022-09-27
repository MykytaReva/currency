from rest_framework.reverse import reverse
from rest_framework.test import APIClient
import pytest

from app.settings.settings import EMAIL_HOST_USER


def test_contactus_get():
    client = APIClient()
    response = client.get(reverse('api-v1:contactus-list'))
    assert response.status_code == 200
    assert response.json()['count']


def test_contactus_post_empty():
    client = APIClient()
    response = client.post(reverse('api-v1:contactus-list'), data={})
    assert response.status_code == 400
    assert response.json() == {
        'email_to': ['This field is required.'],
        'subject': ['This field is required.'],
        'message': ['This field is required.']
    }


@pytest.mark.parametrize(
    ['email', 'subject', 'message'],
    (
        ('nikitarevaya@co.uk', '---dffdfd-_-ef', 2122),
        ('mykReva@yahoo.com', '34342!@#%3sdf4l@c.c', 'ssss'),
        ('ibragim@d.it', '34342dsfsdf2234l@c.c', 23)
    )
)
def test_contactus_post_correct(client, email, subject, message):
    client = APIClient()
    data = {
        'email_to': email,
        'subject': subject,
        'message': message
    }
    response = client.post(reverse('api-v1:contactus-list'), data=data)
    assert response.status_code == 201


@pytest.mark.parametrize(
    ['email', 'subject', 'message'],
    (
        ('nikitarevaya!co.uk', '---dffdfd-_-ef', 2122),
        ('mykReva@yahoo.c', '34342!@#%3sdf4l@c.c', 'ssss'),
        ('ibragim@d.i', '34342dsfsdf2234l@c.c', 23)
    )
)
def test_contactus_post_incorrect(client, email, subject, message):
    client = APIClient()
    data = {
        'email_to': email,
        'subject': subject,
        'message': message
            }
    response = client.post(reverse('api-v1:contactus-list'), data=data)
    assert response.status_code == 400
    assert response.json() == {'email_to': ['Enter a valid email address.']}


@pytest.mark.parametrize(
    ['email', 'subject', 'message'],
    (
        ('nikitarevaya@co.uk', '---dffdfd-_-ef', 2122),
        # ('mykReva@yahoo.com', '34342!@#%3sdf4l@c.c', 'ssss'),
        ('ibragim@d.it', '34342dsfsdf2234l@c.c', 23)
    )
)
def test_contactus_send_email(client, mailoutbox, email, subject, message):
    client = APIClient()
    data = {
        'email_to': email,
        'subject': subject,
        'message': message
            }
    response = client.post(reverse('api-v1:contactus-list'), data=data)
    assert response.status_code == 201
    assert len(mailoutbox) == 1
    assert mailoutbox[0].from_email == EMAIL_HOST_USER
    assert mailoutbox[0].body == str(data['message'])
    assert mailoutbox[0].subject == str(data['subject'])
