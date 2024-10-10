from django.test import TestCase
from django.urls import reverse, resolve
from .views import (HomeView, 
                    AboutView, 
                    contact)

from .forms import ContactUsForm

class TestUrl(TestCase):
    """
    def test_url_home(self):
        url = reverse("root:home")
        self.assertEqual(resolve(url).func.view_class, HomeView)

    def test_url_contact(self):
        url = reverse("root:contact")
        self.assertEqual(resolve(url).func, contact)
    """

    def test_form_true_contact(self):
        form = ContactUsForm(data={
            "name"  : "hamid",
            "email" : "absc@test.com",
            "subject" : "test",
            "message" : "test"
        })
        self.assertTrue(form.is_valid())

    def test_form_false_contact(self):
        form = ContactUsForm(data={
            "name"  : "hamid",
            "email" : "abscest.com",
            "subject" : "test",
            "message" : "test"
        })
        self.assertFalse(form.is_valid())




