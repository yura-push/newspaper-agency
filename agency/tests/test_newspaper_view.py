from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from agency.forms import NewspaperSearchForm
from agency.models import Newspaper, Topic

NEWSPAPER_URL = reverse("agency:newspaper-list")


class PublicNewspaperTest(TestCase):
    def test_login_required(self):
        res = self.client.get(NEWSPAPER_URL)
        self.assertNotEqual(res.status_code, 200)


class PrivateNewspaperTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser",
            password="password",
        )
        topic1 = Topic.objects.create(
            name="Test topic 1"
        )
        topic2 = Topic.objects.create(
            name="Test topic 2"
        )
        self.client.force_login(self.user)
        self.newspaper1 = Newspaper.objects.create(
            title="Test1",
            content="Test content 1",
            published_date="2024-01-01",
            topic=topic1,
        )
        self.newspaper2 = Newspaper.objects.create(
            title="Test2",
            content="Test content 2",
            published_date="2024-01-02",
            topic=topic2,
        )

    def test_retrieve_newspapers(self):
        response = self.client.get(NEWSPAPER_URL)

        self.assertEqual(response.status_code, 200)

        newspapers = Newspaper.objects.all()
        self.assertEqual(
            list(response.context["newspaper_list"]),
            list(newspapers)
        )

        self.assertTemplateUsed(response, "agency/newspaper_list.html")

    def test_newspaper_get_context_data(self):
        response = self.client.get(NEWSPAPER_URL, {"title": "test"})

        self.assertEqual(response.status_code, 200)
        self.assertIn("search_form", response.context)
        self.assertIsInstance(
            response.context["search_form"], NewspaperSearchForm
        )
        self.assertEqual(
            response.context_data["search_form"].initial["title"], "test"
        )

    def test_get_query_with_no_filters(self):
        response = self.client.get(NEWSPAPER_URL)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.newspaper1.title)
        self.assertContains(response, self.newspaper2.title)

    def test_get_query_with_filters(self):
        response = self.client.get(
            NEWSPAPER_URL, {"title": self.newspaper1.title}
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.newspaper1.title)
        self.assertNotContains(response, self.newspaper2.title)
