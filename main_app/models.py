from django.db import models
from django.db.models import JSONField


class Person(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)  # change to PhoneNumberField from \
    # https://github.com/stefanfoulis/django-phonenumber-field (?)
    email = models.EmailField()
    profile_page = models.URLField()

    def __str__(self):
        return f"{self.name} | {self.phone}"


class Lecturer(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    degree = models.CharField(max_length=50)
    position = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.person.name} | {self.degree}"


class Author(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.person}"


class Course(models.Model):
    full_name = models.CharField(max_length=150)
    short_name = models.CharField(max_length=50)
    short_description = models.CharField(max_length=150)
    full_description = models.TextField()
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.short_name}"


class Presentation(models.Model):  # topic
    name = models.CharField(max_length=150)
    # slides = models.ManyToManyField(Slide)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return f"{self.name}"


class Slide(models.Model):
    number = models.IntegerField()
    header = models.CharField(max_length=150)
    content_type = models.CharField(max_length=4)  # text / demo
    content = models.TextField()
    presentation = models.ForeignKey(Presentation, on_delete=models.CASCADE, blank=True, null=True)
    extra_params = JSONField(blank=True, null=True)  # Для хранения параметров, передаваемых matlab функции

    def __str__(self):
        return f"{self.number} | {self.header[:10]}"
