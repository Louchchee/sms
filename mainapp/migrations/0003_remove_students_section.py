# Generated by Django 3.2.5 on 2021-07-18 15:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20210718_2028'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='students',
            name='section',
        ),
    ]
