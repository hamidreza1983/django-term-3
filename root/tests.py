from django.test import TestCase, Client
from django.urls import reverse, resolve
from .views import (HomeView, 
                    AboutView, 
                    contact)


from services.models import Comments
from .forms import ContactUsForm
from services.forms import CommentsForm
from accounts.models import CustomUser
import requests

class TestUrl(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(email="testtest@test.com", password="H@midreza62")


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

    def test_form_comment(self):

        form = CommentsForm(data={
            "user"  : self.user,
            "product_name" : "abscest.com",
            "message" : "test"
        })
        self.assertTrue(form.is_valid())

    def test_model_user(self):
        self.assertEqual(self.user.email, "testtest@test.com")

    def test_model_comment(self):
        comment = Comments.objects.create(user=self.user, product_name="s3", message="test")
        self.assertEqual(comment.message, "test")

    def test_model_comment(self):
        comment = Comments.objects.create(user=self.user, product_name="s3", message="test")
        self.assertTrue(Comments.objects.filter(user=self.user).exists())

    def test_response_home(self):
        url = reverse("root:home")
        c = Client()
        response = c.get(url)
        self.assertEqual(response.status_code, 200)

    def test_template_home(self):
        url = reverse("root:home")
        c = Client()
        response = c.get(url)
        self.assertTemplateUsed(response, template_name="root/index.html")

    def test_template_content_home(self):
        url = reverse("root:home")
        c = Client()
        response = c.get(url)
        if "totam" not in str(response.content):
            raise AssertionError("content may be change")
        

    def test_response_contact_302(self):
        url = reverse("root:contact")
        c = Client()
        response = c.get(url)
        self.assertEqual(response.status_code, 302)

    def test_response_contact_200(self):
        url = reverse("root:contact")
        c = Client()
        c.force_login(self.user)
        response = c.get(url)
        self.assertEqual(response.status_code, 200)









