from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

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
    latitude = models.DecimalField(max_digits=9, decimal_places=6, default=0.3476)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, default=32.5825)
    link = models.CharField(max_length=400)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.facility_name


class Quiz(models.Model):
    title = models.CharField(max_length=400)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)


class Question(models.Model):
    class AnswerOptions(models.TextChoices):
        YES = 'YES', _('Yes')
        NO = 'NO', _('No')
        SOMETIMES = 'SOMETIMES', _('Sometimes')

    content = models.TextField()
    answer = models.CharField(max_length=200, choices=AnswerOptions.choices, default=AnswerOptions.YES)
    quiz = models.ForeignKey(Quiz, on_delete=models.DO_NOTHING)
    difficulty = models.IntegerField(default=1, validators=[MaxValueValidator(5), MinValueValidator(1)])
    position = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
