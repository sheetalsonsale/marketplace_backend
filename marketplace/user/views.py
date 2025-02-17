from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import customer
from .serializers import CustomerModelSerializer

class UserView(APIView):
    def post(self, request):
        serializer = CustomerModelSerializer(data=request.data)  # Validate incoming data
        if serializer.is_valid():
            serializer.save()  # Save to the database
            return Response({"message": "User created successfully!", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return validation errors
