from django.contrib import admin

from app.models import Video, Category, Article, Organization, District, Quiz, Question, FAQ, FAQRating

admin.site.register(Category)
admin.site.register(Video)
admin.site.register(Article)
admin.site.register(Organization)
admin.site.register(District)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(FAQ)
admin.site.register(FAQRating)