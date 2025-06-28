from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer

from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome to Little Lemon API</h1>")

# Create your views here.
def index(request):
  return render(request, 'index.html', {})

# Handles GET (list) and POST (create)
class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

# Handles GET (retrieve), PUT (update), DELETE (delete)
class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
