from django.contrib import admin

from app.models import Video, Category, Article

admin.site.register(Category)
admin.site.register(Video)
admin.site.register(Article)
