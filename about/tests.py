from django.test import RequestFactory, TestCase
from django.urls import resolve, reverse

from .models import About


class AboutPageTests(TestCase):
    def get_about_response(self):
        path = reverse("about")
        request = RequestFactory().get(path)
        return resolve(path).func(request)

    def test_about_page_displays_the_latest_about_entry(self):
        About.objects.create(title="About Us", content="A little about our blog.")

        response = self.get_about_response()

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "About Us")
        self.assertContains(response, "A little about our blog.")
        self.assertContains(response, 'href="/about/"')

    def test_about_page_handles_missing_entry(self):
        response = self.get_about_response()

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "About information is not available yet.")
