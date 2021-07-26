# Generated by Django 3.2.5 on 2021-07-26 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_grade_mark'),
    ]

    operations = [
        migrations.AddField(
            model_name='mark',
            name='session_year',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.sessionyear'),
        ),
        migrations.AlterField(
            model_name='mark',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
    ]
