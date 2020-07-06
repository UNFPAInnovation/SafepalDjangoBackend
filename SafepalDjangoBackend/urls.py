from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from app.views import VideosView, ArticlesView, OrganizationView, DistrictView, QuizView, QuestionView, FAQView, FAQRatingView
from django.conf.urls.static import static
from SafepalDjangoBackend import settings
from django.urls import path, re_path, include
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

schema_view = get_schema_view(
    openapi.Info(
        title="Safepal Django API",
        default_version='v1',
        contact=openapi.Contact(email="pkigenyi@outbox.co.ug"),
        license=openapi.License(name="Copy Right"),
    ),
    # change this in debug mode to localhost:8000
    url='https://webdashboard.safepal.co/api/v1/',
    public=True,
    permission_classes=(permissions.IsAuthenticated,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path(r'auth/', include('djoser.urls.base')),
    path(r'auth/', include('djoser.urls.authtoken')),
    path(r'api/v1/videos', VideosView.as_view(), name='video'),
    path(r'api/v1/articles', ArticlesView.as_view(), name='article'),
    path(r'api/v1/organizations', OrganizationView.as_view(), name='organization'),
    path(r'api/v1/districts', DistrictView.as_view(), name='district'),
    path(r'api/v1/quizzes', QuizView.as_view(), name='quiz'),
    path(r'api/v1/questions', QuestionView.as_view(), name='question'),
    path(r'api/v1/faqs', FAQView.as_view(), name='faq'),
    path(r'api/v1/faqratings', FAQRatingView.as_view(), name='faqratings'),
    url(r'^chat', TemplateView.as_view(template_name='chat_reply.html')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# place the wagtail urls afters media root because they will interfere with the image url
urlpatterns += [re_path(r'', include(wagtailadmin_urls))]
