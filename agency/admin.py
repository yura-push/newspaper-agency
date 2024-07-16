from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from agency.models import Topic, Newspaper, Redactor


@admin.register(Newspaper)
class NewspaperAdmin(admin.ModelAdmin):
    list_display = ["title", "content", "published_date", "topic",]
    list_filter = ["topic", ]
    search_fields = ["title", ]


admin.site.register(Topic)
admin.site.register(Redactor, UserAdmin)
