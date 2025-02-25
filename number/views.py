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

# Update your views here


class NumberUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Number.objects.all()
    serializer_class = NumberSerializers
    lookup_field = 'pk'

    def put(self, request, *args, **kwargs):
        instance = self.get_object()  # Fetch the object
        data = request.data  # Get incoming data

        # Update only the provided fields
        if 'entry' in data:
            instance.entry = data['entry']
        if 'price' in data:
            instance.price = data['price']
        if 'discount' in data:
            instance.discount = data['discount']

        instance.save()  # Save updated fields
        serializer = NumberSerializers(instance)  # Serialize updated object
        return Response({"message": "Updated Successfully", "data": serializer.data}, status=status.HTTP_200_OK)
# Delete your views    
class NumberDeleteAPIView(generics.DestroyAPIView):
    queryset = Number.objects.all()
    serializer_class = NumberSerializers
    lookup_field = 'pk'

    def put(self, request, *args, **kwargs):
        instance = self.get_object()  # Fetch the object
        instance.delete()
        return Response({"message": "Deleted Successfully"}, status=status.HTTP_204_NO_CONTENT)
