from django.shortcuts import render
from rest_framework import generics, viewsets 
from rest_framework.permissions import IsAuthenticated
#from rest_framework.decorators import api_view, permission_classes
from . import serializers
from . import models

# Create your views here.


def index(request):
    return render(request,'index.html',{})

class MenuItem(generics.ListCreateAPIView):
    queryset = models.Menu.objects.all()
    serializer_class = serializers.MenuSerializer




class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Menu.objects.all()
    serializer_class = serializers.MenuSerializer


class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = models.Booking.objects.all()
    serializer_class = serializers.BookingSerializer


