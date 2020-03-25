from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from app.models import Video
from app.serializers import VideoSerializer


class VideosView(ListCreateAPIView):
    """
    Lists and creates Videos.
    """
    serializer_class = VideoSerializer
    queryset = Video.objects.all()
