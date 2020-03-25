from rest_framework import serializers
from app.models import Video, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)


class VideoSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=False, read_only=True)

    class Meta:
        model = Video
        fields = ('title', 'category', 'description', 'thumbnail', 'url', 'rating', 'createdAt')


