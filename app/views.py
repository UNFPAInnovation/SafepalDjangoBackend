
from django.forms import DecimalField
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
from app.models import Video, Article, Organization, District, Quiz, Question, FAQ, FAQRating
from app.serializers import VideoSerializer, ArticleSerializer, OrganizationSerializer, DistrictSerializer, \
    QuizSerializer, QuestionSerializer, FAQSerializer, FAQRatingSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from SafepalDjangoBackend.settings import SHEET_FILES_FOLDER
from .extractor import  extract_excel_data
from geopy.distance import geodesic
from rest_framework.renderers import JSONRenderer
from rest_framework import status

class VideosView(ListCreateAPIView):
    """
    Lists and creates Videos.
    """
    parser_classes = [MultiPartParser, FormParser]
    serializer_class = VideoSerializer
    queryset = Video.objects.all()


class ArticlesView(ListCreateAPIView):
    """
    Lists and creates Articles.
    """
    parser_classes = [MultiPartParser, FormParser]
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

    
class FAQRatingView(ListCreateAPIView):
    """
    Lists and creates FAQRating.
    """
    serializer_class = FAQRatingSerializer
    queryset = FAQRating.objects.all()


class CSOUploadView(ListCreateAPIView):
     serializer_class = OrganizationSerializer

     def get(self, request, format=None, **kwargs):
        # location = (SHEET_FILES_FOLDER + "tester.xls")
        location = (SHEET_FILES_FOLDER + "CSOlist.xls")
        extract_excel_data(location)

        return HttpResponse("Successfully Extrated CSOs")


          
class CurrentLocationView(ListCreateAPIView):
    """
    lists distructs within the provided coordinates
    """
    serializer_class = OrganizationSerializer
    def post(self, request):
        coordinates = request.data
        lat = coordinates["lat"]
        long = coordinates["lng"]
        coords_1=(lat, long)
        queryset = Organization.objects.all().values('facility_name','phone_number', 'latitude','longitude')
        orgunits=[]
        for cso in queryset:
            lat = cso["latitude"]
            lng = cso["longitude"]
            coords_2=(lat,lng)
            distance=geodesic(coords_1, coords_2).km
            orgunits.append({
                "facility_name":cso["facility_name"],
                "phone_number":cso["phone_number"],
                "distance":distance
            })
        newlist = sorted(orgunits,key=lambda d: d['distance'])  
        org_units = newlist[:10]
        return Response({"org_units":org_units}, status=status.HTTP_200_OK)



          