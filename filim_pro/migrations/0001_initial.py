# Generated by Django 4.0.1 on 2022-03-27 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='registration',
            fields=[
                ('unique_id', models.AutoField(primary_key=True, serialize=False)),
                ('firstname', models.CharField(default='null', max_length=100)),
                ('lastname', models.CharField(default='null', max_length=100)),
                ('email', models.CharField(default='null', max_length=255)),
                ('password', models.CharField(default='null', max_length=500)),
                ('phone', models.CharField(default='null', max_length=15)),
                ('profile_photo', models.ImageField(blank=True, upload_to='user_images/')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('active', 'Active')], default='active', max_length=15)),
            ],
        ),
    ]
