# Generated by Django 3.2.6 on 2021-08-09 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0025_alter_invoice_creation_timestamp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('author', models.CharField(max_length=40)),
                ('ISBN', models.CharField(max_length=40)),
                ('publication', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_date', models.DateTimeField(auto_now_add=True)),
                ('return_date', models.DateTimeField()),
                ('issued', models.BooleanField(default=False)),
                ('book_issued', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.book')),
                ('issue_student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.student')),
            ],
        ),
    ]
