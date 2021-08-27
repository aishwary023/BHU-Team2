from django.shortcuts import render
from rest_framework import viewsets
from .serializers import StockSerializer
from rest_framework import status
from rest_framework.response import Response
from .models import Stock
from rest_framework.generics import ListCreateAPIView


# Create your views here.

class StockView(ListCreateAPIView):
  queryset = Stock.objects.none()
  serializer_class = StockSerializer

  def get_queryset(self):
    queryset = Stock.objects.all()
    return queryset

  def create(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response("Successfully added all entries", status.HTTP_201_CREATED)
