from django.contrib import admin
from .models import Movie

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    