# Generated by Django 3.2.9 on 2022-11-01 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utube_app', '0006_author_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='phone_verified',
            field=models.BooleanField(default=False, null=True),
        ),
    ]