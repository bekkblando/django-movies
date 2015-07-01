from django.contrib import admin

from .models import Rater, Movie, Review, Avgmovrate
# Register your models here.

admin.site.register(Rater)
admin.site.register(Movie)
admin.site.register(Review)
admin.site.register(Avgmovrate)