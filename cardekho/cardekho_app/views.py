from django.shortcuts import render
from .models import carlist, showroomlist, review
from rest_framework import status, viewsets

#from django.http import JsonResponse
#for rest_framework
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from .serializers import carserializer, GETshowroomserializer, POSTshowroomserializer, ShowroomSerializer, reviewserializer


class showroom_view(APIView):
    
    def get(self, request):
            showroom = showroomlist.objects.all()
            serializer = GETshowroomserializer(showroom, many = True)
            return Response(serializer.data)
    def post(self, request):
            serializer = POSTshowroomserializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

@api_view(['GET', 'POST'])
def car_list_view(request):
    if request.method == 'GET':
        try:
            car = carlist.objects.all()
        except:
            return Response(status = status.HTTP_404_NOT_FOUND)
        serializer = carserializer(car, many = True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = carserializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
         

@api_view(['GET','PUT','DELETE'])
def car_detail_view(request, pk):
#READ REQUEST
        if request.method == 'GET':
                try:
                    car = carlist.objects.get(pk = pk)
                except:
                    return Response(status = status.HTTP_404_NOT_FOUND)
                serializer = carserializer(car)
                return Response(serializer.data)

        #CREATE/POST REQUEST
        if request.method == 'PUT':
                car = carlist.objects.get(pk = pk)
                serializer = carserializer(car, data = request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                else:
                    return Response(serializer.errors)

        if request.method == 'DELETE':
                car = carlist.objects.get(pk = pk)
                car.delete()
                return Response(status = status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def review_view(request):
    if request.method == 'GET':
        try:
            queryset = review.objects.all()
        except:
            return Response({'error':'not present'}, status = status.HTTP_404_NOT_FOUND)
        
        serializer = reviewserializer(queryset, many = True)
        return Response(serializer.data)


class CarReviewAPIView(APIView):
    def get(self, request, pk):
        try:
            car = carlist.objects.get(pk=pk)
            reviews = car.reviews.all()
            serializer = reviewserializer(reviews, many=True)
            data = {
                "car": {
                    "id": car.id,
                    "model": car.model,
                },
                "reviews": serializer.data
            }
            return Response(data, status=status.HTTP_200_OK)
        except carlist.DoesNotExist:
            return Response({"message": "Car not found"}, status=status.HTTP_404_NOT_FOUND)

class ShowroomReviewAPIView(APIView):
    def get(self, request, showroom_id):
        try:
            showroom = showroomlist.objects.get(pk=showroom_id)
            cars = showroom.cars.all()
            reviews = review.objects.filter(cars__in=cars)
            serializer = reviewserializer(reviews, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except showroomlist.DoesNotExist:
            return Response({"message": "Showroom not found"}, status=status.HTTP_404_NOT_FOUND)
        

def get_cars_in_showroom_view(request, pk):
    try:
        # Get the showroom object based on the provided showroom_id
        showroom = get_object_or_404(showroomlist, pk=pk)
        
        # Query the carlist model to get cars associated with the showroom
        cars_in_showroom = carlist.objects.filter(showroom=showroom)
        
        # Prepare data to be returned in JSON format
        cars_data = []
        for car in cars_in_showroom:
            cars_data.append({
                'model': car.model,
                'description': car.description,
                'chassisnumber': car.chassisnumber,
                'price': car.price,
                
            })
        
        # Return JSON response with cars data
        return JsonResponse({'cars': cars_data}, status=200)
    
    except showroomlist.DoesNotExist:
        # Handle the case where the showroom with the given ID doesn't exist
        return JsonResponse({'error': 'Showroom not found'}, status=404)