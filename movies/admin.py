from django.contrib import admin
from .models import Movie, Genre, Director, Actor

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("name", "genre", "director", "release_date", "score")

    list_filter = ("genre", "score")

    search_fields = ("name",)

    readonly_fields = ('created_at', 'updated_at')

    filter_horizontal = ('actors',)
    
admin.site.register(Genre)
admin.site.register(Director)
admin.site.register(Actor)
