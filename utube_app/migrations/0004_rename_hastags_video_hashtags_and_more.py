# Generated by Django 4.0.6 on 2022-10-09 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utube_app', '0003_rename_comments_comment_rename_likes_like'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='hastags',
            new_name='hashtags',
        ),
        migrations.AlterField(
            model_name='author',
            name='subscribed_to',
            field=models.ManyToManyField(through='utube_app.Subscription', to='utube_app.author'),
        ),
        migrations.AlterField(
            model_name='video',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
