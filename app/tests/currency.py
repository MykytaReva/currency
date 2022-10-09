from rest_framework.reverse import reverse
import pytest


@pytest.mark.django_db
def test_user_create(client):
    data = {
        'email': 'lennonthe@beatles.com',
        'password1': 'johnpassword',
        'password2': 'johnpassword',
    }
    response = client.post(reverse('accounts:signup'), data=data)
    assert response.status_code == 302
    # breakpoint()


def test_contactus_get(client):
    response = client.get(reverse('currency:contactus_create'))
    assert response.status_code == 200


def test_contactus_empty(client):
    response = client.post(reverse('currency:contactus_create'), data={})
    assert response.status_code == 200
    assert response.context_data['form'].errors == {'email_to': ['This field is required.'],
                                                    'subject': ['This field is required.'],
                                                    'message': ['This field is required.']
                                                    }


def test_contactus_post_isvalid(client,  mailoutbox):
    data = {
        'email_to': 'nikitareva@yahoo.com',
        'subject': 'Invitation',
        'message': 'Hi'
            }
    response = client.post(reverse('currency:contactus_create'), data=data)
    assert response.status_code == 302
    assert len(mailoutbox) == 1
    # assert mailoutbox[0].subject == 'ContactUs From Currency Project'


@pytest.mark.parametrize(
    ['email', 'subject', 'message'],
    (
        ('nikitarevayahoo.com', '3434234l@c.c', 'wwwwww'),
        ('nikitare@vayahoo,com', '343423sdf4l@c.c', 'ssss'),
        (3333, '34342dsfsdf2234l@c.c', 23)
    )
)
def test_contactus_post_invalid(client, email, subject, message):
    data = {
        'email_to': email,
        'subject': subject,
        'message': message
            }

    response = client.post(reverse('currency:contactus_create'), data=data)
    assert response.status_code == 200
    assert response.context_data['form'].errors == {'email_to': ['Enter a valid email address.']}
