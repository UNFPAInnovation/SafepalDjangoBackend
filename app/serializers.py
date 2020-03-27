from rest_framework import serializers
from app.models import Video, Category, Article, Organization, District


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)


class VideoSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=False, read_only=True)
    category_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Video
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=False, read_only=True)
    category_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Article
        fields = '__all__'


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ('name',)


class OrganizationSerializer(serializers.ModelSerializer):
    district = DistrictSerializer(many=False, read_only=True)
    district_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Organization
        fields = '__all__'
