import datetime

from django.db import models

from django import forms

DAY_OF_THE_WEEK = (
    ('1', 'Понедельник'),
    ('2', 'Вторник'),
    ('3', 'Среда'),
    ('4', 'Четверг'),
    ('5', 'Пятница'),
    ('6', 'Суббота'),
    ('7', 'Воскресение'),
)


class Room(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=100)
    description = models.TextField(default="", blank=True, null=True)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    objects = models.Manager()
    teacher = models.ForeignKey('users.Teacher', default="", on_delete=models.SET_NULL, null=True)
    room = models.ForeignKey(Room, default="", on_delete=models.SET_NULL, null=True)
    day = models.CharField(choices=DAY_OF_THE_WEEK, max_length=20)
    # day = forms.MultipleChoiceField(choices=DAY_OF_THE_WEEK)
    start_time = models.TimeField(default=datetime.time(12, 0), blank=True, null=True, max_length=10)
    end_time = models.TimeField(default=datetime.time(12, 0), blank=True, null=True, max_length=10)
    students = models.ManyToManyField('users.Child', default="")
    description = models.TextField(default="", blank=True, null=True)

    def __str__(self):
        return self.room.name + " " + self.day + str(self.start_time)
