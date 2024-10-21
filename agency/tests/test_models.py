from django.contrib.auth import get_user_model
from django.test import TestCase

from agency.models import Newspaper, Topic


class ModelsTests(TestCase):
    def test_topic_str(self):
        topic = Topic.objects.create(
            name="Test",
        )
        self.assertEqual(
            str(topic),
            f"{topic.name}"
        )

    def test_redactor_str(self):
        redactor = get_user_model().objects.create(
            username="test",
            password="Test123",
            first_name="Test_first",
            last_name="Test_last",
        )
        self.assertEqual(
            str(redactor),
            f"{redactor.username} ({redactor.first_name} {redactor.last_name})"
        )

    def test_newspaper_str(self):
        topic = Topic.objects.create(
            name="Test"
        )
        newspaper = Newspaper.objects.create(
            title="Test",
            content="test content",
            published_date="2025-01-01",
            topic=topic
        )
        self.assertEqual(
            str(newspaper),
            f"{newspaper.title} {newspaper.content} ({newspaper.published_date})"
        )

    def test_create_redactor_with_years_of_experience(self):
        username = "test"
        password = "Test123"
        years_of_experience = 3
        redactor = get_user_model().objects.create_user(
            username=username,
            password=password,
            years_of_experience=years_of_experience,
        )
        self.assertEqual(redactor.username, username)
        self.assertEqual(redactor.years_of_experience, years_of_experience)
        self.assertTrue(redactor.check_password(password))
