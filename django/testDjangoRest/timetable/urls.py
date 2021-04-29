from django.urls import path, include

from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('rooms', views.RoomViewAPI)
router.register('lessons', views.LessonViewAPI)

urlpatterns = [
    path('', include(router.urls))
]