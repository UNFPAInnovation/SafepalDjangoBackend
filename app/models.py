from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=400)

    def __str__(self):
        return self.name


class Video(models.Model):
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=400)
    description = models.TextField()
    thumbnail = models.CharField(max_length=600)
    url = models.CharField(max_length=600)
    rating = models.IntegerField(default=5)
    duration = models.IntegerField(default=3)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Article(models.Model):
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=400)
    content = models.TextField()
    questions = models.TextField()
    thumbnail = models.CharField(max_length=600)
    rating = models.IntegerField(default=5)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class District(models.Model):
    name = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Organization(models.Model):
    facility_name = models.CharField(max_length=400)
    phone_number = models.CharField(max_length=400)
    district = models.ForeignKey(District, on_delete=models.DO_NOTHING)
    address = models.CharField(max_length=300)
    open_hour = models.CharField(max_length=100)
    close_hour = models.CharField(max_length=100)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    link = models.CharField(max_length=400)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.facility_name
