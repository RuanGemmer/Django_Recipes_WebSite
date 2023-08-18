from django.contrib import admin
from recipes import models


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    ...


@admin.register(models.Recipe)
class RecepiAdmin(admin.ModelAdmin):
    ...
