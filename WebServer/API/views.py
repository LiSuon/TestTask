from django.shortcuts import render
from django.http.response import JsonResponse
from .models import *

def foods(request):
    category = FoodCategory.objects.filter(food__is_publish=True).distinct()
    serializer = FoodListSerializer(category, many=True)

    return JsonResponse(serializer.data, safe=False)