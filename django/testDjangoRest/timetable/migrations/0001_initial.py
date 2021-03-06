# Generated by Django 3.2 on 2021-04-29 11:33

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, default='', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('1', 'Понедельник'), ('2', 'Вторник'), ('3', 'Среда'), ('4', 'Четверг'), ('5', 'Пятница'), ('6', 'Суббота'), ('7', 'Воскресение')], max_length=20)),
                ('start_time', models.TimeField(blank=True, default=datetime.time(12, 0), max_length=10, null=True)),
                ('end_time', models.TimeField(blank=True, default=datetime.time(12, 0), max_length=10, null=True)),
                ('description', models.TextField(blank=True, default='', null=True)),
                ('room', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to='timetable.room')),
                ('students', models.ManyToManyField(default='', to='users.Child')),
                ('teacher', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.teacher')),
            ],
        ),
    ]
