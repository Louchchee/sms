# Generated by Django 3.2.5 on 2021-07-26 11:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_auto_20210726_1633'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='student_code',
        ),
        migrations.AlterField(
            model_name='enroll',
            name='enroll_code',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
