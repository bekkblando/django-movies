from django.contrib import admin

from .models import Link, Movie, Rater
# Register your models here.

admin.site.register(Link)
admin.site.register(Movie)
admin.site.register(Rater)