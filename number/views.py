from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
# Create your views here.
from .serializers import NumberSerializers
from .models import Number

class NumberListCreateAPIView(generics.ListCreateAPIView):
    queryset = Number.objects.all()
    serializer_class = NumberSerializers

    def post(self, request, *args, **kwargs):
        serializer = NumberSerializers(data=request.data)
        if serializer.is_valid():
            if (len(serializer.validated_data['entry']) != 10):
                return Response("Not Valid Number", status=status.HTTP_200_OK)
            
            serializer.save()
            return Response("Created", status=status.HTTP_201_CREATED)

        return Response("Bro", status=status.HTTP_400_BAD_REQUEST)



