from django.shortcuts import render, get_object_or_404
from rest_framework.viewsets import ModelViewSet

from main_app.models import Lecturer, Person, Presentation, Course, Author, Slide, Section
from main_app.serializers import LecturerSerializer, PersonSerializer, CourseSerializer, SlideSerializer, \
    PresentationSerializer


# main_app/views.py

# Create your views here.


class LecturerViewSet(ModelViewSet):
    queryset = Lecturer.objects.all()
    serializer_class = LecturerSerializer


class PersonViewSet(ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class SlideViewSet(ModelViewSet):
    queryset = Slide.objects.all()
    serializer_class = SlideSerializer


class PresentationViewSet(ModelViewSet):
    queryset = Presentation.objects.all()
    serializer_class = PresentationSerializer


def presentation_view(request):
    queryset = Presentation.objects.all()
    return render(request, 'presentation.html', {"presentation_objects": queryset})


def section_view(request):
    queryset = Section.objects.all()
    return render(request, 'section.html', {"section_objects": queryset})


def presentation_detail_view(request, presentation_id):
    presentation = get_object_or_404(Presentation, pk=presentation_id)
    print(presentation.id)
    slides = presentation.slide_set.all()
    return render(request, 'presentation_detail.html', {"presentation": presentation, "slides": slides})


def index(request):
    return render(request, 'index.html')
