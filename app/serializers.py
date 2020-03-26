from rest_framework import serializers
from app.models import Video, Category, Article, Organization


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


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'
