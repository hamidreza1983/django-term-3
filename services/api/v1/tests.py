from rest_framework.test import APIClient
import pytest


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

@pytest.mark.django_db
class TestApi:

    def test_view_services(self, client, api_url_services):
        response = client.get(api_url_services)
        assert response.status_code == 200

    # def test_create_object_on_services(self):
    #     data = {
    #         "name" : "testsdcfgbsfgdb",
    #         "title" : "test",
    #         "content" : "test",
    #         "description" : "test",
    #         "price" : 2000,
    #         "generals" : ["best price",],
    #         "category" : ["travel",],
    #     }
    #     c = APIClient()
    #     url = "http://127.0.0.1:8000/services/api/v1/services"
    #     response = c.post(url, data=data)
    #     assert response.status_code == 201

    def test_view_team(self, client, api_url_team):
        response = client.get(api_url_team)
        assert response.status_code == 201