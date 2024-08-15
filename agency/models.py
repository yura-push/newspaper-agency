from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

from newspaper_agency import settings


class Topic(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name


class Redactor(AbstractUser):
    years_of_experience = models.IntegerField(null=True)

    class Meta:
        ordering = ("username", )

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"

    def get_absolute_url(self):
        return reverse("agency:redactor-detail", args=[str(self.id)])


class Newspaper(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    published_date = models.DateTimeField()
    topic = models.ForeignKey(
        Topic,
        on_delete=models.CASCADE,
        related_name="newspapers"
    )
    publishers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="newspapers"
    )

    class Meta:
        ordering = ("title",)

    def __str__(self):
        return f"{self.title} {self.content} ({self.published_date})"

    def get_absolute_url(self):
        return reverse("agency:newspaper-detail", args=[str(self.id)])
