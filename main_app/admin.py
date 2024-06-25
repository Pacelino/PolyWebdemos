from django.contrib import admin

from main_app.models import Lecturer, Person

# Register your models here.

admin.site.register(Lecturer)
admin.site.register(Person)