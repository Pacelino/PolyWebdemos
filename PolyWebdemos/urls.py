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
from main_app.views import LecturerViewSet, PersonViewSet, CourseViewSet, SlideViewSet, PresentationViewSet, \
presentation_view, presentation_detail_view, index, approx_demo_view, demo_dispatcher_view, section_view, section_detail_view

router = routers.DefaultRouter()
# api урлы в которых лежат данные модели
router.register('lecturer', LecturerViewSet)
router.register('person', PersonViewSet)
router.register('course', CourseViewSet)
router.register('presentation', PresentationViewSet)
router.register('slide', SlideViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('presentation/', presentation_view),
    path('presentations/<int:presentation_id>/', presentation_detail_view, name='presentation_detail'),
    path('section/', section_view),
    path('sections/<int:section_id>/', section_detail_view, name='section_detail'),
    path('presentations/<int:presentation_id>/<int:demonstration_id>/', demo_dispatcher_view, name='demo_dispatcher'),
    path('', index, name='index'),
    path('api/', include(router.urls)),
    path('approx_demo/', approx_demo_view, name='approx_demo'),
    path('course/<int:course_id>/', views.course_detail, name='course_detail')

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)