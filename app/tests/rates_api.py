from rest_framework.reverse import reverse
from rest_framework.test import APIClient


def test_rates_get():
    client = APIClient()
    response = client.get(reverse('api-v1:rate-list'))
    assert response.status_code == 200
    assert response.json()['count']
    assert response.json()['results']


def test_rates_post_empty():
    client = APIClient()
    response = client.post(reverse('api-v1:rate-list'), data={})
    assert response.status_code == 400
    assert response.json() == {
        'buy': ['This field is required.'],
        'sale': ['This field is required.'],
        'source': ['This field is required.']
    }
