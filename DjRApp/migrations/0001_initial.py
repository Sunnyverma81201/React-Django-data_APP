# Generated by Django 4.0.5 on 2022-06-28 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ObjectDetectionData',
            fields=[
                ('images_name', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('objects_detected', models.CharField(max_length=600)),
                ('timestamp', models.DateField()),
            ],
        ),
    ]
