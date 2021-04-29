from django.urls import path, include

from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('child', views.ChildViewAPI)
router.register('parent', views.ParentViewAPI)
router.register('teacher', views.TeacherViewAPI)

urlpatterns = [
    path('', include(router.urls))
]
