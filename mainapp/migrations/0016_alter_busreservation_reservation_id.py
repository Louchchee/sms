# Generated by Django 3.2.5 on 2021-09-30 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0015_alter_busreservation_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='busreservation',
            name='reservation_id',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
