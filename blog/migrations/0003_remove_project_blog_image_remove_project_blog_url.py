# Generated by Django 4.0 on 2021-12-12 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_project_blog_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project_blog',
            name='image',
        ),
        migrations.RemoveField(
            model_name='project_blog',
            name='url',
        ),
    ]
