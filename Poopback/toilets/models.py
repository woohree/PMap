from django.db import models
from django.conf import settings


class Toilet(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=254)
    management = models.CharField(max_length=100)
    male_big = models.IntegerField()
    male_small = models.IntegerField()
    male_disabled_big = models.IntegerField()
    male_disabled_small = models.IntegerField()
    male_child_big = models.IntegerField()
    male_child_small = models.IntegerField()
    female_big = models.IntegerField()
    female_disabled_big = models.IntegerField()
    female_child_big = models.IntegerField()
    is_unisex = models.BooleanField()
    is_24 = models.BooleanField()
    is_emergency = models.BooleanField()
    is_cctv = models.BooleanField()
    is_diaper = models.BooleanField()
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_toilets', blank=True)


class Review(models.Model):
    content = models.TextField()
    rate = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    toilet = models.ForeignKey(Toilet, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews', blank=True)