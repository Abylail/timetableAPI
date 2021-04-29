from .models import Parent, Child, Teacher

from rest_framework import viewsets

from .serializers import ParentSerializer, ChildSerializer, TeacherSerializer


class ChildViewAPI(viewsets.ModelViewSet):
    queryset = Child.objects.all()
    serializer_class = ChildSerializer


class ParentViewAPI(viewsets.ModelViewSet):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer


class TeacherViewAPI(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
