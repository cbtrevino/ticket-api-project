from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.shortcuts import  get_object_or_404
from .serializers import EventSerializer
from .models import Event, Category

# Create your views here.
class EventViewSet(viewsets.ViewSet):

    queryset = Event.objects.all()
    #serializer_class = EventSerializer

    def list(self, request):
        serializer_class = EventSerializer(self.queryset, many=True)
        return Response(serializer_class.data)

    def retrieve(self, request, pk=None):
        event = get_object_or_404(self.queryset, pk=pk)
        serializer_class = EventSerializer(event)
        return Response(serializer_class.data)