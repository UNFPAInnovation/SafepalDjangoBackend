from wagtail.contrib.modeladmin.options import modeladmin_register, ModelAdmin, ModelAdminGroup
from wagtail.core import hooks

from .models import *


class ArticleAdmin(ModelAdmin):
    model = Article
    menu_label = "Articles"
    menu_icon = "doc-full"
    menu_order = 100
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("title", "thumbnail", "created_at")
    list_filter = ("category",)
    search_fields = ("title",)


class VideoAdmin(ModelAdmin):
    model = Video
    menu_label = "Video"
    menu_icon = "media"
    menu_order = 200
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("title", "url", "created_at")
    list_filter = ("category",)
    search_fields = ("title",)


class QuizAdmin(ModelAdmin):
    model = Quiz
    menu_label = "Quizzes"
    menu_icon = "form"
    menu_order = 100
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("title", "thumbnail", "created_at")
    list_filter = ("article", "category")
    search_fields = ("content",)


class QuestionAdmin(ModelAdmin):
    model = Question
    menu_label = "Questions"
    menu_icon = "list-ol"
    menu_order = 200
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("position", "content", "answer", "quiz")
    list_filter = ("quiz",)
    search_fields = ("content",)


class QuizGroup(ModelAdminGroup):
    menu_label = "QuizGroup"
    menu_icon = "list-ol"
    menu_order = 300
    items = (QuizAdmin, QuestionAdmin)


class OrganizationAdmin(ModelAdmin):
    model = Organization
    menu_label = "Organizations"
    menu_icon = "group"
    menu_order = 400
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("facility_name", "district", "phone_number", "created_at")
    list_filter = ("district",)
    search_fields = ("facility_name",)


class CategoryAdmin(ModelAdmin):
    model = Category
    menu_label = "Categories"
    menu_icon = "pick"
    menu_order = 500
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("name",)
    search_fields = ("name",)


class DistrictAdmin(ModelAdmin):
    model = District
    menu_label = "Districts"
    menu_icon = "site"
    menu_order = 600
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("name",)
    search_fields = ("name",)


modeladmin_register(ArticleAdmin)
modeladmin_register(VideoAdmin)
modeladmin_register(QuizGroup)
modeladmin_register(OrganizationAdmin)
modeladmin_register(CategoryAdmin)
modeladmin_register(DistrictAdmin)


@hooks.register('construct_main_menu')
def hide_default_explorer_menu(request, menu_items):
    menu_items[:] = [item for item in menu_items if item.name not in ['settings', 'images', 'documents', 'reports', 'explorer']]