# Generated by Django 3.2.5 on 2021-07-30 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_studentappearedexam'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentattendance',
            name='status',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='teacherattendance',
            name='status',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
