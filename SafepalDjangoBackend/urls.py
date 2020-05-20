from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view

from app.views import VideosView, ArticlesView, OrganizationView, DistrictView, QuizView, QuestionView
from django.conf.urls.static import static
from SafepalDjangoBackend import settings
schema_view = get_swagger_view(title='Safepal Django API')


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', schema_view),
    path('admin/', admin.site.urls),
    path(r'auth/', include('djoser.urls.base')),
    path(r'auth/', include('djoser.urls.authtoken')),
    path(r'api/v1/videos', VideosView.as_view(), name='video'),
    path(r'api/v1/articles', ArticlesView.as_view(), name='article'),
    path(r'api/v1/organizations', OrganizationView.as_view(), name='organization'),
    path(r'api/v1/districts', DistrictView.as_view(), name='district'),
    path(r'api/v1/quizzes', QuizView.as_view(), name='quiz'),
    path(r'api/v1/questions', QuestionView.as_view(), name='question'),
]

urlpatterns += static(settings.MEDIA_ROOT, document_root=settings.MEDIA_ROOT)