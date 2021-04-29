from django.db import models


class Person(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=100)
    description = models.TextField(default="", blank=True, null=True)
    phone = models.CharField(max_length=15, default="", blank=True, null=True)

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Parent(Person):
    pass


class Child(Person):
    article = models.ForeignKey(Parent, on_delete=models.CASCADE, default="")


class Teacher(Person):
    pass
