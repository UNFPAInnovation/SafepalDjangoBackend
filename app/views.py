from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from app.models import Video, Article, Organization, District, Quiz, Question, FAQ
from app.serializers import VideoSerializer, ArticleSerializer, OrganizationSerializer, DistrictSerializer, \
    QuizSerializer, QuestionSerializer, FAQSerializer


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


class QuestionView(ListCreateAPIView):
    """
    Lists and creates Question.
    """
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()


class FAQView(ListCreateAPIView):
    """
    Lists and creates FAQ.
    """
    serializer_class = FAQSerializer
    queryset = FAQ.objects.all()