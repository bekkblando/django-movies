from django.contrib import admin

from .models import Links, Movies, Rater
# Register your models here.

admin.site.register(Links)
admin.site.register(Movies)
admin.site.register(Rater)