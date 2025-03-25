from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Messages
from .serializers import MessageSerializer
# Create your views here.
@api_view(['GET'])
def messages_list(request):
    messages = Messages.objects.all()
    serializer = MessageSerializer(messages, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def create_message(request):
    serializer = MessageSerializer(data=request.data)
    if(serializer.is_valid()):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)