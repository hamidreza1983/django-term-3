from django.test import TestCase
from django.urls import reverse, resolve
from .views import ServiceView, ServiceDetaiView

class TestUrl(TestCase):
    def test_url_services(self):
        url = reverse("services:services")
        self.assertEqual(resolve(url).func.view_class, ServiceView)

    def test_url_service_detail(self):
        url = reverse("services:services-detail", kwargs={"pk":150})
        self.assertEqual(resolve(url).func.view_class, ServiceDetaiView)

    def test_url_service_by_category(self):
        url = reverse("services:list_by_category", kwargs={"category":"test"})
        self.assertEqual(resolve(url).func.view_class, ServiceView)
