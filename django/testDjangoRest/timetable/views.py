from .models import Lesson, Room

from rest_framework import viewsets

from .serializers import RoomSerializer, LessonSerializer


class LessonViewAPI(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class RoomViewAPI(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
