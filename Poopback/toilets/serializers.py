from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Toilet, Review


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('id', 'content', 'rate', 'created_at', 'updated_at')


class ToiletSerializer(serializers.ModelSerializer):

    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Toilet
        fields = ('pk', 'name', 'address', 'management', 'male_big', 'male_small', 'male_disabled_big', 'male_disabled_small', 
        'male_child_big', 'male_child_small', 'female_big', 'female_disabled_big', 'female_child_big', 'is_unisex', 'is_24',
        'is_emergency', 'is_cctv', 'is_diaper','reviews')
        read_only_fields = ('reviews',)
        

class ToiletListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Toilet
        fields = ('pk', 'name', 'address', 'x', 'y',)