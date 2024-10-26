from rest_framework.test import APIClient
import pytest, json
from django.urls import reverse


@pytest.fixture
def client():
    c = APIClient()
    return c

@pytest.fixture
def api_url_services():
    url = "http://127.0.0.1:8000/services/api/v1/services"
    return url

@pytest.fixture
def api_url_team():
    url = "http://127.0.0.1:8000/services/api/v1/team"
    return url

@pytest.fixture
def api_url_detail_services():
    url = "http://127.0.0.1:8000/services/api/v1/services/1"
    return url


@pytest.mark.django_db
class TestApi:

    def test_view_services(self, client, api_url_services):
        response = client.get(api_url_services)
        assert response.status_code == 200

    def test_post_services(self, client, api_url_services):
        url = api_url_services
        data = {
                "name": "q22",
                "content": "w22",
                "title": "e22",
                "description": "d22",
                "price": 200
            }
        response = client.post(url, data)
        assert response.status_code == 201

    def test_view_detail_services(self, client, api_url_detail_services, api_url_services):
        data = {
                "name": "q2",
                "content": "w2",
                "title": "e2",
                "description": "d2",
                "price": 200
            }
        client.post(api_url_services, data)
        response = client.get(api_url_detail_services)
        assert response.status_code == 200

    def test_view_team(self, client, api_url_team):
        response = client.get(api_url_team)
        assert response.status_code == 200