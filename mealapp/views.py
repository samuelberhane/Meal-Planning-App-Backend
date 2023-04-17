from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Meal, FoodItem
from .serializers import MealSerializer, FoodItemSerializer

# Get all meals or create a new meal
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def meal_list(request):
    if request.method == 'GET':
        meals = Meal.objects.filter(user=request.user)
        serializer = MealSerializer(meals, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = MealSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Get, update, or delete a single meal
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def meal_detail(request, meal_id):
    meal = get_object_or_404(Meal, pk=meal_id)
    if request.method == 'GET':
        serializer = MealSerializer(meal)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = MealSerializer(instance=meal, data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        meal.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Get all food items or create a new food item
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def food_item_list(request):
    if request.method == 'GET':
        food_items = FoodItem.objects.all()
        serializer = FoodItemSerializer(food_items, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = FoodItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Get, update, or delete a single food item
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def food_item_detail(request, food_item_id):
    food_item = get_object_or_404(FoodItem, pk=food_item_id)
    if request.method == 'GET':
        serializer = FoodItemSerializer(food_item)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = FoodItemSerializer(instance=food_item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        food_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# get all meal for single user
@api_view(["GET"])
def getMealsByUserId(request, userId):
    meals = Meal.objects.filter(user_id=userId)
    serializer = MealSerializer(meals, many=True)
    return Response(serializer.data)
