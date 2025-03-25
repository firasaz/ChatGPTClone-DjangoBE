from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .serializers import ChatSerializer
from .models import Chat

# Create your views here.
@api_view(['GET'])
def chats_list(request):
    chats = Chat.objects.all()
    serializer = ChatSerializer(chats, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
    

@api_view(['POST'])
def create_new_chat(request):
    serializer = ChatSerializer(data=request.data) # serialize the body of the request
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
