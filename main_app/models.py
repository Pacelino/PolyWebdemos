from django.contrib.postgres.indexes import GinIndex
from django.contrib.postgres.search import SearchVectorField
from django.db import models
from django.db.models import JSONField


class Person(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)

    def __str__(self):
        return f"{self.name}"


class Lecturer(models.Model):
    person = models.OneToOneField(Person, on_delete=models.DO_NOTHING)
    degree = models.CharField(max_length=50, blank=True)
    position = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    photo = models.ImageField(upload_to='photos', blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return f"{self.person.name} | {self.degree}"


class Author(models.Model):
    person = models.OneToOneField(Person, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.person}"


class Course(models.Model):
    full_name = models.CharField(max_length=150)
    short_name = models.CharField(max_length=50)
    short_description = models.CharField(max_length=150, blank=True)
    full_description = models.TextField(blank=True)
    lecturer = models.ForeignKey(Lecturer, on_delete=models.DO_NOTHING, blank=True)

    def __str__(self):
        return f"{self.short_name}"


class Section(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name}"


class Presentation(models.Model):
    name = models.CharField(max_length=150)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, blank=True, null=True)
    number = models.IntegerField()  # order in section
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING, blank=True)
    courses = models.ManyToManyField(Course, blank=True)

    # search_vector = SearchVectorField()
    #
    # class Meta:
    #     indexes = [GinIndex(fields=['search_vector'])]

    def __str__(self):
        return f"{self.name}"


class Slide(models.Model):
    number = models.IntegerField()
    header = models.CharField(max_length=150, blank=True)
    content = models.TextField()
    presentation = models.ForeignKey(Presentation, on_delete=models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return f"{self.header}"


class Demo(models.Model):
    presentation = models.ForeignKey(Presentation, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name
