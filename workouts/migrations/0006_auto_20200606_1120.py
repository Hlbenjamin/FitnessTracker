# Generated by Django 3.0.6 on 2020-06-06 18:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0005_auto_20200606_1114'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='weight',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='weight',
            name='code',
        ),
    ]