from rest_framework import serializers

from .models import Parent, Child, Teacher


class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = ("id", "name", "phone", "description", "child_set")


class ChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child
        fields = ("id", "name", "phone", "description", "article", "lesson_set")


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ("id", "name", "phone", "description", "lesson_set")
