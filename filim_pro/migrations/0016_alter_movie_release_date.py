# Generated by Django 4.0.1 on 2022-04-05 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filim_pro', '0015_alter_people_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='release_date',
            field=models.DateTimeField(max_length=100),
        ),
    ]
