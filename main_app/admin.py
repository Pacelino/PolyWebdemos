from django.contrib import admin

from main_app.models import Lecturer, Person, Slide, Presentation, Author, Course

# Register your models here.

admin.site.register(Lecturer)
admin.site.register(Person)
admin.site.register(Slide)
admin.site.register(Presentation)
admin.site.register(Author)
admin.site.register(Course)