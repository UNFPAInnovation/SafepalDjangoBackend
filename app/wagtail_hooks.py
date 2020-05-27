from wagtail.contrib.modeladmin.options import modeladmin_register, ModelAdmin

from .models import *


class ArticleAdmin(ModelAdmin):
    model = Article
    menu_label = "Article"
    menu_icon = "pick"
    menu_order = 000
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("title", "thumbnail", "created_at")
    list_filter = ("title",)
    search_fields = ("title",)


class VideoAdmin(ModelAdmin):
    model = Video
    menu_label = "Video"
    menu_icon = "pick"
    menu_order = 100
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("title", "url", "created_at")
    list_filter = ("title",)
    search_fields = ("title",)


modeladmin_register(ArticleAdmin)
modeladmin_register(VideoAdmin)
