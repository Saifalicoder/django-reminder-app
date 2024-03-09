from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Reminder
from .serializers import ReminderSerializer

@api_view(['POST'])
def create_reminder(request):
    serializer = ReminderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'status': 'Reminder saved successfully!'},status=200)
    else:
        return Response(serializer.errors, status=400)