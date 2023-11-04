# Generated by Django 4.2.4 on 2023-10-10 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facultyapp', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentMarks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('marks', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.DeleteModel(
            name='Mark',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]