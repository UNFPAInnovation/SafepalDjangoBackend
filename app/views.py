from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from app.models import Video, Article, Organization, District, Quiz, Question
from app.serializers import VideoSerializer, ArticleSerializer, OrganizationSerializer, DistrictSerializer, \
    QuizSerializer


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


class OrganizationView(ListCreateAPIView):
    """
    Lists and creates Organization.
    """
    serializer_class = OrganizationSerializer
    queryset = Organization.objects.all()


class DistrictView(ListCreateAPIView):
    """
    Lists and creates Districts.
    """
    serializer_class = DistrictSerializer
    queryset = District.objects.all()


class QuizView(ListCreateAPIView):
    """
    Lists and creates Quiz.
    """
    serializer_class = QuizSerializer
    queryset = Quiz.objects.all()
