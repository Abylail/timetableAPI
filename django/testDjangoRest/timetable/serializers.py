from rest_framework import serializers

from .models import Room, Lesson


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ("id", "name", "description", "lesson_set")


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ("id", "teacher", "room", "students", "start_time", "end_time", "day", "description")
