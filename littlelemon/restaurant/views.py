from django.shortcuts import render
from rest_framework import generics, viewsets 
from rest_framework import permissions as permission
from rest_framework.response import Response
from . import serializers
from . import models

# Create your views here.

class MenuItem(generics.ListCreateAPIView):
    queryset = models.Menu.objects.all()
    serializer_class = serializers.MenuSerializer


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Menu.objects.all()
    serializer_class = serializers.MenuSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = models.Booking.objects.all()
    serializer_class = serializers.BookingSerializer
