from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Meal, Rating
from .serializers import MealSerializer, RatingSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404



# Meal CRUD Operations
class MealViewSets(ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer

# Rating CRUD Operations
class RatingViewSets(ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer




