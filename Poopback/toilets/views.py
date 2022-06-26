from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_safe
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.hashers import PBKDF2PasswordHasher

from .models import Toilet, Review

from .serializers import (
    ToiletListSerializer,
    ToiletSerializer,
    ReviewSerializer,
    )


@api_view(['GET'])
def toilet_index(request, x, y):
    toilets = Toilet.objects.all()
    serializer = ToiletListSerializer(toilets, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def toilet_detail(request, toilet_pk):
    toilet = get_object_or_404(Toilet, pk=toilet_pk)
    serializer = ToiletSerializer(toilet)
    return Response(serializer.data)


@api_view(['POST'])
def review_create(request, toilet_pk):
    toilet = get_object_or_404(Toilet, pk=toilet_pk)
    
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        hasher = PBKDF2PasswordHasher()
        password = request.data.password
        serializer.save(toilet=toilet, password=password)

        reviews = toilet.reviews.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT', 'DELETE'])
def review_update_delete(request, toilet_pk, review_pk):
    toilet = get_object_or_404(Toilet, pk=toilet_pk)
    review = get_object_or_404(Review, pk=review_pk)

    def update_review():
        if request.data.password == review.data.password:
            serializer = ReviewSerializer(instance=review, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                reviews = toilet.reviews.all()
                serializer = ReviewSerializer(reviews, many=True)
                return Response(serializer.data)

    def delete_review():
        if request.data.password == review.data.password:
            review.delete()
            reviews = toilet.reviews.all()
            serializer = ReviewSerializer(reviews, many=True)
            return Response(serializer.data)
    
    if request.method == 'PUT':
        return update_review()
    elif request.method == 'DELETE':
        return delete_review()
