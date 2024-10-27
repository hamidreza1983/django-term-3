from rest_framework.test import APIClient
import pytest, json
from django.urls import reverse
from accounts.models import CustomUser
from services.models import Category, Options, Skills


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

@pytest.fixture
def admin_user():
    admin = CustomUser.objects.create_user(email="admin@test.com", password="H@midreza62")
    admin.is_superuser = True
    admin.is_staff = True
    admin.is_verified = True
    admin.save()
    return admin

@pytest.fixture
def normal_user():
    user = CustomUser.objects.create_user(email="user@test.com", password="H@midreza62")
    return user


@pytest.fixture
def skills_object():
    Skills.objects.create(title="test", status=True)
    Skills.objects.create(title="test2", status=True)
    skills = Skills.objects.all()
    return skills

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

    def test_create_team(self, client, api_url_team, admin_user, skills_object):
        client.force_authenticate(user=admin_user)
        data = {
            "profile" : admin_user.id,
            "skills" : [
                skills_object[0].id
                ],
            "description" : "test"
        }
        response = client.post(api_url_team, data=data)
        assert response.status_code == 201

    def test_create_team_with_normal_user(self, client, api_url_team, normal_user, skills_object):
        client.force_authenticate(user=normal_user)
        data = {
            "profile" : normal_user.id,
            "skills" : [
                skills_object[0].id
                ],
            "description" : "test"
        }
        response = client.post(api_url_team, data=data)
        assert response.status_code == 403