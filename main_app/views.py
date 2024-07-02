from django.http import Http404
from django.shortcuts import render, get_object_or_404
from rest_framework.viewsets import ModelViewSet

from SWF.approx_demo import approx_demo
from main_app.forms import ApproxDemoForm, AnotherDemoForm
from main_app.models import Lecturer, Person, Presentation, Course, Author, Slide, Section, Demo
from main_app.serializers import LecturerSerializer, PersonSerializer, CourseSerializer, SlideSerializer, \
    PresentationSerializer, SectionSerializer


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


class SectionViewSet(ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer

def index(request):
    return render(request, 'index.html')



def presentation_view(request):
    queryset = Presentation.objects.all()
    return render(request, 'presentation.html', {"presentation_objects": queryset})


def section_view(request):
    queryset = Section.objects.all()
    return render(request, 'section.html', {"section_objects": queryset})


def presentation_detail_view(request, presentation_id):
    # получает презентацию по presentation_id
    presentation = get_object_or_404(Presentation, pk=presentation_id)
    # достаю все слайды нужной презентации
    slides = presentation.slide_set.all()
    demonstrations = presentation.demo_set.all()
    return render(request, 'presentation_detail.html', {"presentation": presentation, "slides": slides, "demonstrations": demonstrations})


def section_detail_view(request, section_id):
    section = get_object_or_404(Section, pk=section_id)
    presentations = section.presentation_set.all()
    return render(request, 'section_detail.html', {"section": section, "presentations": presentations})


def approx_demo_view(request):
    if request.method == 'POST':
        form = ApproxDemoForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            cleaned_data = form.cleaned_data
            paramtype = cleaned_data['param_type']
            varvalue = float(cleaned_data['var_value'])
            show_pnxi = cleaned_data.get('show_pnxi', False)
            show_pyxim1 = cleaned_data.get('show_pyxim1', False)
            show_pyxip1 = cleaned_data.get('show_pyxip1', False)
            show_pyxi = cleaned_data.get('show_pyxi', False)
            show_hists = cleaned_data.get('show_hists', False)
            px1 = float(cleaned_data['show_px1'])
            num_points = int(cleaned_data['num_points'])
            image_path = approx_demo(
                paramtype=paramtype,
                varvalue=varvalue,
                show_pnxi=show_pnxi,
                show_pyxim1=show_pyxim1,
                show_pyxip1=show_pyxip1,
                show_pyxi=show_pyxi,
                show_hists=show_hists,
                px1=px1,
                num_points=num_points
            )
            data = {'form': form, 'image_path': image_path}
            print(image_path)
            return render(request, 'approx_demo.html', data)
    form = ApproxDemoForm()
    data = {'form': form}
    return render(request, 'approx_demo.html', data)


def another_demo_view(request):
    if request.method == 'POST':
        form = AnotherDemoForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            data = {'form': form}
            return render(request, 'another_demo_view.html', data)
    else:
        form = AnotherDemoForm()
    data = {'form': form}
    return render(request, 'another_demo.html', data)


# функция - диспетчер. Позволяет по динамическому demonstration_id распределять демонстрации
def demo_dispatcher_view(request, demonstration_id, presentation_id):
    presentation = get_object_or_404(Presentation, pk=presentation_id)
    demonstration = get_object_or_404(Demo, pk=presentation_id)

    if demonstration not in presentation.demo_set.all():
        raise Http404("Demo not found")
# этот пример моей задумки. Пока в нем нет смысла.
    if presentation.name == "Entropy":
        if demonstration_id == 1:
            return approx_demo_view(request)
        elif demonstration_id == 2:
            return another_demo_view(request)
    else:
        if demonstration_id == 1:
            return another_demo_view(request)
        elif demonstration_id == 2:
            return another_demo_view(request)

def course_detail(request, course_id):
    # Логика для получения данных о курсе по course_id
    # course = get_course(course_id) - это может быть запрос к базе данных
    context = {
        'course_id': course_id,
        # 'course': course - добавьте курс в контекст, если необходимо
    }
    return render(request, 'course_description.html', context)
