# Generated by Django 4.2.4 on 2023-10-14 21:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0009_rename_subject_studentmarks_course_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='studentmarks',
            table='studentmarks_table',
        ),
    ]