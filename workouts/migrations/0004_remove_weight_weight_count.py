# Generated by Django 3.0.6 on 2020-06-02 00:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0003_weight_weight_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weight',
            name='weight_count',
        ),
    ]
