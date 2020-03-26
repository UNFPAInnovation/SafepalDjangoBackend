from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view

from app.views import VideosView, ArticlesView

schema_view = get_swagger_view(title='GetIN Django API')

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', schema_view),
    path('admin/', admin.site.urls),
    path(r'auth/', include('djoser.urls.base')),
    path(r'auth/', include('djoser.urls.authtoken')),
    path(r'api/v1/videos', VideosView.as_view(), name='videos'),
    path(r'api/v1/articles', ArticlesView.as_view(), name='article'),
]
