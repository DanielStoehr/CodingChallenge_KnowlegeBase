from django.test import TestCase

# Create your tests here.
from django.urls import reverse

from knowledge.models import KnowlegeBase


class Test_Knowledge(TestCase):
    def test_open_start(self):
        response = self.client.get(reverse("start"))
        self.assertEqual(response.status_code, 200)

    def test_open_add(self):
        response = self.client.get(reverse("add"))
        self.assertEqual(response.status_code, 200)

    def test_create_correct_entry(self):
        data = {
            "title": "Testtitle",
            "text": "mycontent",
            "author": "testAuthor",
        }
        response = self.client.post(reverse("add"), data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(KnowlegeBase.objects.all()), 1)

    def test_create_incorrect_entry(self):
        data = {
            "title": "Testtitle",
            "text": "mycontent",
        }
        response = self.client.post(reverse("add"), data)
        print(response.status_code)

        self.assertEqual(response.status_code, 404)
