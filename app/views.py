from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from app.models import Video, Article
from app.serializers import VideoSerializer, ArticleSerializer


class VideosView(ListCreateAPIView):
    """
    Lists and creates Videos.
    """
    serializer_class = VideoSerializer
    queryset = Video.objects.all()


class ArticlesView(ListCreateAPIView):
    """
    Lists and creates Articles.
    """
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
