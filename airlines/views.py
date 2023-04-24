from django.shortcuts import render
from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from airlines.models import Airline
from airlines.serializers import AirlineSerializer
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET', 'POST', 'DELETE'])
def airline_list(request):
    if request.method == 'GET':
        airlines = Airline.objects.all()
        
        name = request.GET.get('name', None)
        if name is not None:
            airlines = airlines.filter(name__icontains=name)
        
        airline_serializer = AirlineSerializer(airlines, many=True)
        return JsonResponse(airline_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        airline_data = JSONParser().parse(request)
        airline_serializer = AirlineSerializer(data=airline_data)
        if airline_serializer.is_valid():
            airline_serializer.save()
            return JsonResponse(airline_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(airline_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Airline.objects.all().delete()
        return JsonResponse({'message': '{} Airlines were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def airline_detail(request, pk):
    try: 
        airline = Airline.objects.get(pk=pk) 
    except Airline.DoesNotExist: 
        return JsonResponse({'message': 'The airline does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        airline_serializer = AirlineSerializer(airline) 
        return JsonResponse(airline_serializer.data) 
 
    elif request.method == 'PUT': 
        airline_data = JSONParser().parse(request) 
        airline_serializer = AirlineSerializer(airline, data=airline_data) 
        if airline_serializer.is_valid(): 
            airline_serializer.save() 
            return JsonResponse(airline_serializer.data) 
        return JsonResponse(airline_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        airline.delete() 
        return JsonResponse({'message': 'Airline was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET'])
def airline_list_published(request):
    airlines = Airline.objects.filter(published=True)
        
    if request.method == 'GET': 
        airlines_serializer = AirlineSerializer(airlines, many=True)
        return JsonResponse(airlines_serializer.data, safe=False)
        # 'safe=False' for objects serialization    