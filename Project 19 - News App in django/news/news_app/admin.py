from django.contrib import admin

# Register your models here.
from .models import NewsContent, Review, Tag

admin.site.register(NewsContent)
admin.site.register(Review)
admin.site.register(Tag)