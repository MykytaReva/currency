# from rest_framework.reverse import reverse
# import pytest
# from rest_framework.test import APIRequestFactory


# def test_api_contactus_get(client):
#     response = client.get(reverse('api-v1:contactus-list'))
#     factory = APIRequestFactory()
#     request = factory.post('/notes/', {'title': 'new idea'})
#     assert response.status_code == 200


# @pytest.mark.django_db
# def test_contact_us_create(client):
#     data = {
#         'email_to':'lennonthe@beatles.com',
#         'subject': 'Team meeting today!',
#         'message': 'You are invited for today event at 7p.m.',
#     }
#     response = client.post(reverse('accounts:signup'), data=data)
#     assert response.status_code == 302
#     breakpoint()
