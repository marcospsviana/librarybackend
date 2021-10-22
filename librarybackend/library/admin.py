from django.contrib import admin
from .models import PublishCompany


@admin.register(PublishCompany)
class AdminPublishCompany(admin.ModelAdmin):
    fields = ["name"]
