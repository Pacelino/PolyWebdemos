"""
URL configuration for PolyWebdemos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from rest_framework import routers

from main_app import views

router = routers.DefaultRouter()
# api урлы в которых лежат данные модели
router.register('lecturer', views.LecturerViewSet)
router.register('person', views.PersonViewSet)
router.register('course', views.CourseViewSet)
router.register('presentation', views.PresentationViewSet)
router.register('slide', views.SlideViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),


    path('presentation/', views.presentation_view),
    path('presentations/<int:presentation_id>/', views.presentation_detail_view, name='presentation_detail'),
    path('presentations/<int:presentation_id>/<int:demonstration_id>/', views.demo_dispatcher_view,
         name='demo_dispatcher'),

    path('section/', views.section_view),
    path('sections/<int:section_id>/', views.section_detail_view, name='section_detail'),

    path('course/<int:course_id>/', views.course_detail_view, name='course_detail'),

    path('lecturer/', views.lecturer_view),
    path('lecturers/<int:lecturer_id>', views.lecturer_detail_view, name='lecturer_detail'),

    path('', views.index, name='index'),

    path('api/', include(router.urls)),
    path('approx_demo/', views.approx_demo_view, name='approx_demo'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
