# Generated by Django 5.0.6 on 2024-07-06 08:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_remove_person_phone_remove_person_profile_page_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slide',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='slide',
            name='extra_params',
        ),
    ]
