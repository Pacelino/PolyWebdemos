from rest_framework.serializers import ModelSerializer

from main_app.models import Lecturer, Person, Course, Slide, Presentation, Section, Author


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class LecturerSerializer(ModelSerializer):
    class Meta:
        model = Lecturer
        fields = '__all__'


class PersonSerializer(ModelSerializer):
    class Meta:
        model = Person
        fields = ['id', 'name', 'email']


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class SlideSerializer(ModelSerializer):
    class Meta:
        model = Slide
        fields = '__all__'


class PresentationSerializer(ModelSerializer):
    class Meta:
        model = Presentation
        fields = '__all__'


class SectionSerializer(ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'
