# Generated by Django 3.2.19 on 2023-07-01 21:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0006_alter_comment_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='rating',
        ),
    ]
