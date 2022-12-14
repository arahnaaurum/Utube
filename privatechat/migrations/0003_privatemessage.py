# Generated by Django 3.2.9 on 2022-10-24 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('privatechat', '0002_delete_publicchat'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrivateMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.IntegerField()),
                ('recepient', models.IntegerField()),
                ('time_creation', models.DateTimeField(auto_now_add=True)),
                ('text', models.TextField()),
                ('isRead', models.BooleanField(default=False)),
            ],
        ),
    ]
