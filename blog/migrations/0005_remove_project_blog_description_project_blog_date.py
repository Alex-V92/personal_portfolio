# Generated by Django 4.0 on 2021-12-12 19:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_project_blog_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project_blog',
            name='description',
        ),
        migrations.AddField(
            model_name='project_blog',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 12, 22, 35, 43, 358902)),
        ),
    ]