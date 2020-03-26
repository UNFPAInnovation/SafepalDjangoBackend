from django.contrib import admin

from app.models import Video, Category, Article, Organization

admin.site.register(Category)
admin.site.register(Video)
admin.site.register(Article)
admin.site.register(Organization)
